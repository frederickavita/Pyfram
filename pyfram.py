""""
Pyfram version 1.0.O
Pyfram it's mini library brython inspire from w3.js(https://www.w3schools.com/w3js/default.asp) and Angular 
Pyfram it's easy to use
Pyfram can  import html, sort content of any html element
hide or show any html element, add or remove classes any html elment 
many more...
the goal is to have a module that allows with very few code to do a lot of things
for example for hides elements : 
from pyfram import hide 
hide('p') #Hide all <p> elements
or 
To remove multiple classes from an element
from pyfram import remove_class 

remove_class('#London','class1 class2') #Remove both "class1" and "class2" from an element with id="London"
"""


from browser import document as doc, window as win

timeout = ""


def hide(selector):
    """
    style display hide
    selector : str css selector.
    ex: hide('p'), hide('h2'), hide('#london')
    """
    element = doc.querySelectorAll(selector)
    if element:
        for i in range(len(element)):
            element[i].style.display = "none"


def show(selector):
    """
    style display show
    selector : str css selector.
    ex: show('p'), show('h2'), show('#london')
    """
    element = doc.querySelectorAll(selector)
    if element:
        for i in range(len(element)):
            element[i].style.display = "block"


def toggle_show(selector):
    """
    Toggle Hide and Show Using Element
    selector: str css selector.
    ex: toggle_show('#London') for id 
        toggle_show('h2') for div tag 
        toggle_show('.city') for class 
    """
    element = doc.querySelectorAll(selector)
    if element:
        for i in range(len(element)):
            if element[i].style.display == "none":
                element[i].style.display = "block"
            else:
                element[i].style.display = "none"


def add_style(element, property, value):
    """
    Add a CSS property value
    element :str selector css like #London, .London etc..
    property: str property css like "background-color", color,display etc..
    value: str value css like "red" for color property
    ex : add_style('#London','background-color','red')
         add_style('h2','background-color','red')
         add_style('.city','background-color','red')
    """
    element = doc.querySelectorAll(element)
    if element:
        for i in range(len(element)):
            element[i].style[property] = value


def add_class(selector, list_class):
    """
    Add a class name to the div element
    selector : str css style  selector
    list_class: str class name  or list class name.
    add_class(selector,'class') or add_class(selector,'class1 class2...')
    ex: add_class('#London','marked') 
        add_class('#London','w3-red w3-xlarge')
    """
    element = doc.querySelectorAll(selector)
    if element:
        liste = list_class.split()
        for i in range(len(element)):
            for r in range(len(liste)):
                if element[i].classList.contains(liste[r]) is False:
                    element[i].className += ' ' + liste[r]


def remove_class(selector, list_class):
    """
    Remove a class or Remove multiple classes
    selector :str css style  selector
    list_class:str class name  or list class name 
    remove_class(selector,'class') or remove_class(selector,'class1 class2...')
    remove_class('#London','marked')
    remove_class('#London','w3-panel w3-red')
    """
    element = doc.querySelectorAll(selector, list_class)
    if element:
        liste = list_class.split()
        for i in range(len(element)):
            for r in range(len(liste)):
                if element[i].classList.contains(liste[r]):
                    element[i].classList.remove(liste[r])


def toggle_class(selector, class1, class2=None):
    """
    selector : str, selector css 
    class1: str 
    class2: str    
    Toggle a class (on/off):
    toggle_class(selector,'class')
    ex : toggle_class('#London','marked')
    Toggle between two classes:
    toggle_class(selector, 'class1, class2')
    toggle_class(#London','w3-red','w3-green')
    """
    element = doc.querySelectorAll(selector)
    if len(element):
        if class2 is None:
            for i in range(len(element)):
                if element[i].classList.contains(class1):
                    element[i].classList.remove(class1)
                else:
                    element[i].className += ' ' + class1
        else:
            for i in range(len(element)):
                if element[i].classList.contains(class1):
                    element[i].classList.remove(class1)
                    element[i].className += ' ' + class2
                else:
                    if element[i].classList.contains(class2):
                        element[i].classList.remove(class2)
                        element[i].className += ' ' + class1


def filter_html(ide, selector, id_input):
    """
    Filter Lists to Search for a name in the input field.
    ide: str css style  like #id01
    selector: str tag div like li
    id input: str id like #id
    ex: filter('#id01', 'li', #input)
    trigger event:
    with brython: document['input'].bind('input', funct)
    """
    element1 = doc.querySelectorAll(ide)
    element2 = doc.querySelectorAll(selector)
    inpu = doc[id_input]
    if element1:
        for i in range(len(element1)):
            for r in range(len(element2)):
                if element2[r].innerHTML.upper().find(inpu.value.upper()) != -1:
                    element2[r].style.display = ""
                else:
                    element2[r].style.display = "none"


def sort_html(ide, selector, sortvalue=None):
    """
    Sort elements
    ide: str selector id like #ide
    selector: str css  
    sortvalue: str css selector , None to default
    example :sort('#id01', 'li')
    example : sort_html('#myTable', '.item', 'td:nth-child(1)')
    """
    bytt = ''
    element1 = doc.querySelectorAll(ide)
    for i in range(len(element1)):
        for j in range(2):
            cc = 0
            y = 1
            while y == 1:
                y = 0
                b = doc[ide[1:]].querySelectorAll(selector)
                for x in range(len(b) - 1):
                    bytt = 0
                    if sortvalue:
                        v1 = b[x].querySelector(
                            sortvalue).innerHTML.lower()
                        v2 = b[x +
                               1].querySelector(sortvalue).innerHTML.lower()
                    else:
                        v1 = b[x].innerHTML.lower()
                        v2 = b[x + 1].innerHTML.lower()
                    if j == 0 and v1 > v2 or j == 1 and v1 < v2:
                        bytt = 1
                        break
                if bytt == 1:
                    b[x].parentNode.insertBefore(b[x + 1], b[x])
                    y = 1
                    cc += 1
            if cc > 0:
                break


def ajax_html(ev, element, callback):
    """"
    Callback response ajax from include method
    Arguments:
    ev: ajax event 
    element: div element
    callback: function
    """

    if ev.target.readyState == 4:
        if ev.target.status == 200:
            element.innerHTML = ev.target.responseText
            if ev.target.status == 400:
                element.innerHTML = "Page not found."
            element.removeAttribute("py-include-html")
            if callback:
                callback()
            include()


def include_methode(cb):
    """
    include method search div attribute py-include-html
    in id div then send ajax request
    cb is function
    """

    z = doc.getElementsByTagName("*")
    for i in range(len(z)):
        elmnt = z[i]
        file = elmnt.getAttribute("py-include-html")
        if file:
            flore = elmnt
            xhttp = win.XMLHttpRequest.new()
            xhttp.addEventListener(
                "readystatechange", lambda ev: ajax_html(ev, flore, cb))
            xhttp.open("GET", file, True)
            xhttp.send()
            return


def control(id, data):
    """check if controller function in globals"""
    if "controller" in globals():
        globals()["search_attrib"](id, data)


def render_html_alone(data, check):
    """ return parse html """
    for x in data.keys():
        check.innerHTML = check.innerHTML.replace("{" + x + "}", str(data[x]))


def render_html(bracelet, key_princ, element, data, inner, id):
    o = ""
    h = []
    hj = []
    libre = []
    elmn = ''.join(element)
    for z in bracelet:
        if len(o) == 0:
            if z:
                for x in data[key_princ]:
                    o = elmn.replace("{" + z + "}", x[z])
                    libre.append(o)
        else:
            if h:
                libre = h
                h = []
            for i in range(len(data[key_princ])):
                hj = libre[i].replace("{" + z + "}", data[key_princ][i][z])
                h.insert(i, hj)
    if h:
        libre = h
        h = ''
        libre = ''.join(libre)
        inner.outerHTML = inner.outerHTML.replace(inner.outerHTML, libre)
        control(id, data)
    else:
        if libre:
            libre = ''.join(libre)
            inner.outerHTML = inner.outerHTML.replace(inner.outerHTML, libre)
            control(id, data)


def check_id(id):
    """ function return id """
    if isinstance(id, str):
        return doc[id]
    else:
        return False


def get_attribut(element, attr):
    lo = element.getElementsByTagName("*")
    for i in range(len(lo)):
        if "py-repeat" in lo[i].attrs:
            print(i)
            name = lo[i].attrs[attr]
            del lo[i].attrs[attr]
            outer = lo[i].outerHTML
            return (outer, name, lo[i])
    return False


def search_attrib(id, data):
    check = check_id(id)
    if check:
        ui = get_attribut(check, "py-repeat")
        if ui:
            copy_list = [ui[0]]
            stre = ui[0]
            stre = win.String.new(stre)
            reg = win.RegExp.new("{(.+?)}", "g")
            bracelet = stre.match(reg)
            bracelet = [x.replace("{", "") for x in bracelet]
            bracelet = [x.replace("}", "") for x in bracelet]
            key_princ = ui[1]
            render_html(bracelet, key_princ, copy_list, data, ui[2], id)

        else:
            stre = check.innerHTML
            stre = win.String.new(stre)
            reg = win.RegExp.new("{(.+?)}", "g")
            bracelet = stre.match(reg)
            render_html_alone(data, check)


def http_ajax(ev, readyfunc):
    global controller
    import json
    if ev.target.readyState == 4 and ev.target.status == 200:
        ert = json.loads(ev.target.responseText)
        controller = True
        readyfunc(ert)
    else:
        return False


def http(target, readyfunc, method='GET'):
    if win.XMLHttpRequest:
        httprequest = win.XMLHttpRequest.new()
    else:
        httprequest = win.ActiveXObject("Microsoft.XMLHTTP").new()
    if httprequest:
        if readyfunc:
            httprequest.addEventListener(
                "readystatechange", lambda ev: http_ajax(ev, readyfunc))
            httprequest.open(method, target, True)
            httprequest.send()
            return


def display_http(file, funct):
    http(file, funct)


class Slide:
    current = 1

    @staticmethod
    def getElements(id):
        return doc.querySelectorAll(id)

    @staticmethod
    def style_element(element, val):
        element.style.display = val

    @staticmethod
    def style_elements(elements, val):
        for i in range(len(elements)):
            Slide.style_element(elements[i], val)

    @staticmethod
    def displ(n, selector):
        Slide.style_elements(Slide.getElements(selector), "none")
        l = doc.querySelectorAll(selector)
        Slide.style_element(l[n - 1], "block")

    @staticmethod
    def next(selector, milliseconde):
        Slide.current += 1
        if Slide.current > len(doc.querySelectorAll(selector)):
            Slide.current = 1
        Slide.start(selector, milliseconde)

    @staticmethod
    def previous(selector, milliseconde):
        Slide.current -= 1
        if Slide.current < 1:
            Slide.current = len(doc.querySelectorAll(selector))
        Slide.start(selector, milliseconde)

    @staticmethod
    def start(selector, milliseconde):
        global timeout
        Slide.displ(Slide.current, selector)
        if milliseconde > 0:
            win.clearTimeout(timeout)
            timeout = win.setTimeout(
                Slide.next, milliseconde, selector, milliseconde)


def slide_show(selector, interval=0):
    """"Start slideshow:"

    Arguments:
        selector: str selector  css example:
        html element:
        <img class="nature" src="img_snowtops.jpg">
        <img class="nature" src="img_mountains.jpg">
        <img class="nature" src="img_nature.jpg">

        slide_show(".nature") --


        interval type: integer spedd interval -- example : slide_show(".nature", 0)
        default interval is 0
    """
    if not (not isinstance(interval, int) and not (interval == 0)):
        milliseconde = interval
    else:
        milliseconde = 1000
    Slide.start(selector, milliseconde)


def include(cb=None):
    """
    cb: function -- cb is function callback (default: {None})
    with call back
    def my_call_back():
        print("hello")
    include(my_call_back)

    without call back 
    include()
    """

    include_methode(cb)
