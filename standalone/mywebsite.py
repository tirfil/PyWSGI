from httpd import WebServer

class MyWebSite(WebServer):
    def __init__(self):
        pass
        
    def process(self,environ,start_response,parameters):
        path = environ['PATH_INFO']
        if path.endswith('.css') or path.endswith('.html') or path.endswith('.ico') :
            status = '200 OK'
            try:
                body = open(path[1:]).read()
            except:
                status = '404 NOT FOUND'
                body = "<p>File %s not found</p>" % path
            start_response(status,[('Content-type', 'text/html')])
            return [body]
        elif path == "/":
            status = '200 OK'
            html = """
            <html><head><title>Login page</title><FRAMESET COLS="15%,85%"><FRAME SRC="/login_margin" NAME="margin"><FRAME SRC="/login" NAME="frame"></FRAMESET></head><body></body></html>
            """
            start_response(status,[('Content-type', 'text/html')])
            return([html])
        elif path == "/login_margin":
            status = '200 OK'
            html = """
            <html><head><title>Login page</title><script type="text/javascript">function login() { parent.frame.location="/login"}function registration() {
            parent.frame.location="/registration"}</script></head><body style="background-color:#C0C0C0;"><h1>Links:</h1><a href="javascript:registration()">
            New Registration</a><br /><a href="javascript:login()">Login</a></body></html>
            """
            start_response(status,[('Content-type', 'text/html')])
            return([html])
        elif path == "/login":
            status = '200 OK'
            html = """
            <html><head><title>Login page</title><style type="text/css"> html, body { background-color: #D0C0C0; height: 100%; margin: 0; padding: 0; color: blue; text-align: center; } 
            div#centered { border: 0; background-color: #C0C0D0; height: 25%; width: 30%; position: absolute; left: 35%; top: 33%; color: black; }</style>
            </head><body><div id="centered"><h1>Login</h1><form action="login" method="post" enctype="text/plain"> Email address:<span style="margin-left:6px;"> <input type="text" name="user" /> 
            </span><br /> Password:<span style="margin-left:30px;"> <input type="password" name="password" /> </span><br /><br /> <input type="submit" value="Send">
            <input type="reset" value="Reset"></form></div></body></html>
            """
            start_response(status,[('Content-type', 'text/html')])
            return([html])
        elif path == "/registration":
            status = '200 OK'
            html = """
            <html><head><title>HTML Online Editor Sample</title></head><body><h1 style="text-align: center;">Edition de code HTML</h1><p>Essai de Form
            </p><form action="registration_check" enctype="text/plain" method="post" name="Info"><p><br />Pr&eacute;nom: <input maxlength="20" name="Prenom" size="20" type="text" />
            </p><p>Nom: &nbsp; &nbsp; <input maxlength="20" name="nom" size="20" type="text" /></p><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
            <input name="Soumettre" type="submit" value="Aller" /></p></form></body></html>
            """
            start_response(status,[('Content-type', 'text/html')])
            return([html])
        else:
            start_response('404 NOT FOUND',[('Content-type', 'text/html')])
            text = "<p>path %s is not found</p>" % path
            return [text]
        
mws = MyWebSite()
mws.run(port=8080)