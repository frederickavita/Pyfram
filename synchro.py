'''
Synchro request inspire kivy module:  https://github.com/kivy/kivy/blob/master/kivy/network/urlrequest.py

version: 1.0.0

Synchro request use fetch api to make asynchronous requests ont the 

web et get the result when the request is completed. THe spirit is the 

make request with few code line

The syntax to create a request Post for example it's very simple with brython:


from browser import alert
from synchro import UrlRequest


def response(ev):
    print(ev)

def error(err):
    if err:
        alert(err)


data = {"color": "red"}

ert = {'Accept': 'application/json','Content-Type': 'application/json'}
UrlRequest(url ="http://127.0.0.1:8000/test/default/lse",
            response_type ="json",
            method="POST",header=ert,
            on_error=error,
            on_response=response, 
            body=data)


Only url is mandatory: the rest are optional.
By default the method is GET.
if you use body parameter you must put method on "POST". "GET" or "HEAD" method  
incompatibility with body parameter. 
to the request will be accessible as the parameter called "ev" on
the callback function of the on_success event.By default the response it's text format.


Example without parameter


def response(ev):
    print(ev)

def error(err):
    if err:
        alert(err)


UrlRequest(url ="http://127.0.0.1:8000/test/default/lse, 
            on_error=error,
            on_response=response,")


Example with parameter "GET"



def response(ev):
    print(ev)

def error(err):
    if err:
        alert(err)

UrlRequest(url ="http://127.0.0.1:8000/test/default/lse",
            response_type ="text",
            method="text",
            on_error=error,
            on_response=response, 
            body=data)

'''






from browser import window as win, document as doc
import json

fet = win.fetch #fetch API javascript to call


def Modif(f):
    """function which take object javascript and return python dictionnary """
    js = win.JSON.stringify(f)
    dict_type = json.loads(js)
    return dict_type


class UrlRequest:
    """

    :Parameters:
        url: complete url string
        response_type: format response by default it's text. you can choice : text or json or blob
        example: for text format. In the callback function of the on_success 
        def succes(ev):
            print(ev)
        for json format. The format will be python dictionnary type
        def succes(ev):
            a = (type(ev))
            a --> <class 'dict'>
            you can use like python dict ex : ev['variable']

        for blob format. the format will be blob object
        def succes(ev):
            print(ev.type)
            print(ev.size)

        on_response: callback(result)
        Callback function to call when the result has been fetched.
        on_error: callback(error)
        Callback function to call if an error occurs.
        redirect: "url" domain page from website which send request. 
                  The redirect parametre can be used to redirect to another URL to receive
                  response succes. 
                  all other paramater not compatibility
                  redirect function only accepts text/string format 
                  #login.html
                  example : from synchro import UrlRequest 
                  def error(err):
                      if err:
                         alert(err)
                     UrlRequest(url ="http://127.0.0.1:8000/test/default/lse",
                     response_type="json",
                     redirect="profil.html")
                
                #profil.html
                from synchro import request 
                def succes():
                    if request:
                        print(request)
        method : str, defaults to 'GET'. 
                Other method `DELETE`, HEAD`, `OPTIONS`, `POST`, or `PUT`
                GET and HEAD not compatible with body parameter
        header : This is a Header Interface. dict, defaults to None
                 example :hder =  { 'Content-Type': 'text/plain',
                                    'Accept-Charset' : 'utf-8', 'Accept-Encoding':'gzip,deflate'}
                          UrlRequest(url=url, header=hder)
        mode : str, "navigate", "same-origin", "no-cors", "cors",  default to "cors"
        cache: str,  "default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"
                default to "no-cache"
        credentials: str, "omit", "same-origin", "include" default to None 
        redirect_response :str,  "follow", "error", "manual" , default to "follow"
        referrer_policy :dtr,  "no-referrer","no-referrer-when-downgrade","same-origin","origin","strict-origin","origin-when-cross-origin",
                                        "strict-origin-when-cross-origin","unsafe-url" default to None
        integrity: str,  is a security feature example : sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC default to None
        destination: str, option:  "", "audio", "audioworklet", "document", "embed", "font", "image", "manifest", "object", "paintworklet", "report", "script", "sharedworker", "style",  "track", "video", "worker", "xslt    
                    default to None
        body: dict,  task = {"userId": "1","title": "PYFORM","completed": "False"}
             body not compatible with   "GET", "HEAD" method parameter
        keepalive: Bool, default to False    
        debug: boolean, default to False
        If True, it will use the to print information in console browser                   
    """

    def __init__(self, url,
                 response_type=None,
                 on_response=None,
                 on_error=None,
                 redirect=None,
                 method=None,
                 header=None,
                 mode=None,
                 cache=None,
                 credentials=None,
                 redirect_response=None,
                 referrer_policy=None,
                 integrity=None,
                 destination=None,
                 body=None,
                 keepalive=False,
                 debug=False):
        self.url = url
        self.response_type = response_type
        self.on_response = on_response
        self.on_error = on_error
        self.redirect = redirect
        self.method = method
        self.header = header
        self.mode = mode
        self.cache = cache
        self.integrity = integrity
        self.credentials = credentials
        self.keepalive = keepalive
        self.redirect_response = redirect_response
        self.referrer_policy = referrer_policy
        self.destination = destination
        self.header_new = None
        self.body = body
        self.req = None
        if self.method is None:
            self.send_request()
        else:
            if self.method in ['GET', "POST", "PUT", "PATCH", "DELETE", 'HEAD']:
                self.new_request()


    def new_request(self):
        """ 
        check if the parameter is True and add in dict to generate request Object
        """
        request_dict= {}
        if self.body:
            if isinstance(self.body, dict):
                self.body = win.JSON.stringify(self.body)
        list_sentance = {'method': self.method,
                        "body": self.body,
                        'headers': self.header,
                        'mode': self.mode,
                        'redirect': self.redirect_response,
                        'integrity': self.integrity,
                        'keepalive': self.keepalive,
                        "referrerPolicy": self.referrer_policy,
                        "destination": self.destination,
                        'cache': self.cache}               
        for x in list_sentance.keys():
            if list_sentance[x] != None:
                if x == 'headers':
                    self.header_new = win.Headers.new(list_sentance[x])
                    request_dict[x] = self.header_new
                else:
                    request_dict[x] = list_sentance[x]
        self.req = win.Request.new(
            self.url, request_dict)
        self.send_request()

    def page_redirect(self):
        """redirect page """
        win.location.href = self.redirect

    def redirect_url(self, ev):
        """store response in session storage """
        win.sessionStorage.setItem("request", ev)
        self.page_redirect()

    def response_redirect(self, ev):
        """redirect function only accepts text/string format """
        return ev.text()

    def response(self, ev):
        """Response  have a number of properties and methods that allow us to process 
        the response effectively. For example, each response object has an ok property that checks to see if the
        response is successful. This is based on the HTTP status code 3 , which can be
        accessed using the status property. This will usually be 200 if the response was
        successful, 201 if a resource was created, or 204 when the request is successful
        but no content is returned. The ok property will return true if the status
        property is between 200 and 299. We need to manually check if this happens
        because the promise will only be rejected in the case of a network error, rather
        than something like a “404 page not found error"""
        if ev.ok:
            if self.response_type == "text":
                return ev.text()
            elif self.response_type == "json":
                return ev.json()
            elif self.response_type == "blob":
                return ev.blob()
        else:
            return False


    def send_request(self):
        """
        send the requests according to if redirect function, "GET" or "POST", json response
        string response, blob response etc...
        """
        if self.redirect and self.req is None:
            fet(self.url).then(self.response_redirect).then(
                self.redirect_url).catch(lambda ev: self.on_error(ev.message))
        elif self.redirect is None and self.req is None:
            if self.response_type == "json":
                fet(self.url).then(self.response).then(lambda ev: self.on_response(
                    Modif(ev))).catch(lambda ev: self.on_error(ev.message))
            else:
                fet(self.url).then(self.response).then(self.on_response).catch(
                    lambda ev: self.on_error(ev.message))
        elif self.redirect is None and self.req:
            if self.response_type == "json":
                fet(self.req).then(self.response).then(lambda ev: self.on_response(
                    Modif(ev))).catch(lambda ev: self.on_error(ev.message))
            else:
                fet(self.req).then(self.response).then(self.on_response).catch(
                    lambda ev: self.on_error(ev.message))


def request():
    """ 
    check if response store in session storage.
    allows access to the data in case of redirection function
    """
    if "request" in win.sessionStorage:
        return win.sessionStorage.request
    else:
        return False
