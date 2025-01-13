import wsgiref
import os,webbrowser
from wsgiref.util import setup_testing_defaults,shift_path_info,request_uri
from wsgiref.simple_server import make_server
from jinja2 import Environment, FileSystemLoader
import cgi,sys
import magic,time,uuid
try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs


__version__="0.01"


"""     super eazy web framework    """
"""     jinja template engine     """
""" debugモード, db管理, websockets, gas, session エラーハンドリング準備"""
class request():
    def __init__(self,method,path,ip,ua,host,cookie,header,data,postdata,sessionid):
        self.method=method
        self.path=path
        self.ip=ip
        self.ua=ua
        self.host=host
        self.cookie=cookie
        self.header=header
        self.data=data
        self.post=postdata
        self.item=sessionitem(sessionid)

class mimeset():
    def __init__(self,data,mimetype):
        self.data=data
        self.mime=mimetype

class responce():
    def __init__(self,data,responce):
        self.data=data
        self.datas=responce

class file():
    def __init__(self,filename,download=False,name=None):
        mime = magic.Magic(mime=True)
        self.mimetype=mime.from_file(filename)
        self.download=download
        self.name=name
        self.filename=filename
        if not name:
            self.name=filename
        
def nodatafunc(aa):
    return "NoData"

pagefunc={
    "GET":nodatafunc,
    "POST":nodatafunc,
    "PUT":nodatafunc,
    "DELETE":nodatafunc,
    }

setting={}

setting["template"]="./"

session={}

class sessionitem():
    def __init__(self,sessionid):
        self.session=sessionid
    def __getitem__(self,key):
        global session
        return session[self.session][key]
    def __setitem__(self,key,val):
        global session
        session[self.session][key]=val

def session_set():
    sessionid=str(uuid.uuid4())
    session[sessionid]={}
    return sessionid

def template(filename,**data):
    eenv = Environment(loader=FileSystemLoader('./', encoding='utf8'))
    template = env.get_template(setting["template"]+filename)
    output=template.render(data)
    return output

def get(func):
    global pagefunc
    def wrapper():
        global pagefunc
        pagefunc["GET"]=func
    wrapper()
    return wrapper
def post(func):
    global pagefunc
    def wrapper():
        global pagefunc
        pagefunc["POST"]=func
    wrapper()
    return wrapper
def put(func):
    global pagefunc
    def wrapper():
        global pagefunc
        pagefunc["PUT"]=func
    wrapper()
    return wrapper
def delete(func):
    global pagefunc
    def wrapper():
        global pagefunc
        pagefunc["DELETE"]=func
    wrapper()
    return wrapper
def go(link,timee=0):
    return f'<meta http-equiv="Refresh" content="{timee};URL={link}">'
@get
def samplepage(e):
    print(e.ip)
    return e.ip
apps=""
def sads():
    print(apps)
def cookie_make(name,value):
    cookie = ('Set-Cookie', f'{name}={value}')
    headers.append(cookie)
headers=[]
def app(environ, start_response):
    setup_testing_defaults(environ)
    global apps,headers
    apps=environ
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    wsgi_input = environ["wsgi.input"]
    form = cgi.FieldStorage(fp=wsgi_input, environ=environ, keep_blank_values=True)
    ee=(environ["REQUEST_METHOD"],
                "/".join(request_uri(environ).split("/")[3:]),
                environ["REMOTE_ADDR"],
                environ["HTTP_USER_AGENT"],
                environ["HTTP_HOST"],
                dict([i.split("=") for i in environ["HTTP_COOKIE"].split("; ")]))
    if "." in request_uri(environ):
        pass
    elif not "session" in ee[5]:
        sid=session_set()
        print("set session")
        cookie = ('Set-Cookie', f'session={sid}')
        headers.append(cookie)
    else:
        sid=ee[5]["session"]
        try:
            session[sid]
        except:
            sid=session_set()
            cookie = ('Set-Cookie', f'session={sid}')
            headers.append(cookie)
    e = request(environ["REQUEST_METHOD"],
                "/".join(request_uri(environ).split("/")[3:]),
                environ["REMOTE_ADDR"],
                environ["HTTP_USER_AGENT"],
                environ["HTTP_HOST"],
                dict([i.split("=") for i in environ["HTTP_COOKIE"].split("; ")]),
                environ,
                parse_qs(environ["QUERY_STRING"]),
                {k: form[k].value for k in form},
                sid)
    print(session)
    returns=pagefunc[environ["REQUEST_METHOD"]](e)
    #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

    if type(returns)==dict or type(returns)==list:
        headers = [('Content-type', 'applicaion/json;')]
        ret = [("%s\n" % (text,)).encode("utf-8")
           for text in [str(returns)]]
    elif type(returns)==file:
        stats = os.stat(returns.filename)
        headers = [('Content-type', f'{returns.mimetype};')]
        with open(returns.filename,mode='br') as f:
            ret = [bytes(f.read())]
    elif type(returns)==mimeset:
        headers = [('Content-type', f'{returns.mime};')]
        ret = [bytes(returns.data)]
    elif type(returns)==responce:
        headers = [('Content-type', f'{returns.datas};')]
        ret = [bytes(returns.data)]
    else:
        ret = [("%s\n" % (text,)).encode("utf-8")
           for text in [str(returns)]]
    start_response(status,headers)
    return ret
def run(port):
    with make_server('', port, app) as httpd:
        print(f"Serving on port {port}...")
        httpd.serve_forever()

if __name__=="__main__":
    cli=sys.argv
    if cli[1]=="--set":
        while True:
            time.sleep(int(cli[3]))
            os.system(cli[2])
