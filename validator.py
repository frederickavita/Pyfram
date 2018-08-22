""""
Validators are function used to validate input fields.
version 1.0.0
"""


from browser import document as doc, window as win

# call javascript regex
ema = win.RegExp.new(
    "^[a-z0-9][a-z0-9-_\.]+@([a-z]|[a-z0-9]?[a-z0-9-]+[a-z0-9])\.[a-z0-9]{2,10}(?:\.[a-z]{2,10})?$")


def send_url(ev, url, message_error, message_valid):
    """if response had status 404 it's valid """
    if ev.target.readyState == 4:
        if ev.target.status == 404:
            if message_valid:
                return(True, url, message_valid)
            else:
                return(True, url)
        else:
            return(False, url)


def test_url(url, message_error=None, message_valid=None):
    """Test if url it's valid with ajax call 
        url : str url 
        message_error: str message In case of error
        message valid: str message valid in case it's ok
     """
    request = win.XMLHttpRequest.new()
    request.open('GET', url, True)
    request.addEventListener('onreadystatechange', lambda ev: send_url(
        ev, url, message_error, message_valid))
    request.send()


def number(value, message_error=None, message_valid=None):
    """
    value : value element DOM. Example : document['id].value 
    message_error : str message 
    message_valid: str message 
    function return tuple
    """
    if isinstance(value, (int, float, complex)):
        if message_valid:
            return(True, value, message_valid)
        else:
            return(True, value)
    else:
        return(False, value)


def Boolean(value, message_error=None, message_valid=None):
    """ 
    value : value element DOM. Example : document['id].value 
    message_error : str message 
    message_valid: str message 
    function return tuple
    """
    if isinstance(value, str):
        value = value.lower()
        if value in ('1', 'true', 'yes', 'on', 'enable'):
            if message_valid:
                return(True, message_valid)
            else:
                return (True)
        if value in ('0', 'false', 'no', 'off', 'disable'):
            if message_valid:
                return(False, message_valid)
            else:
                return(False)
        else:
            return("error", message_error)


def email(value, message_error=None, message_valid=None):
    """ 
    value : value element DOM. Example : document['id].value 
    message_error : str message 
    message_valid: str message 
    function return tuple
    """
    if not ema.test(value):
        return (False, "invalid Email", value)
    else:
        if message_valid:
            return(True, message_valid, value)
        else:
            return(True, value)


def url_valid(value, message_error=None, message_valid=None):
    test_url(value, message_error, message_valid)


def lenght(value, min, max, message_error=None, message_valid=None):
    """ 
    min : integer 
    max: integer
    value : value element DOM. Example : document['id].value 
    message_error : str message 
    message_valid: str message 
    function return tuple
    """
    if min is not None and len(value) < min:
        return(False, message_error or 'length of value must be at least %s' % min, value)
    if max is not None and len(value) > max:
        return(False, message_error or 'length of value must be at most %s' % min, value)
    else:
        return(True, message_valid or 'valid', value)
