
#    Copyright 2014 Philippe THIRION
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#from wsgiref.simple_server import make_server
import cgi
import sys

class WebServer:
    def __init__(self):
        pass

    #def entry(self,environ, start_response):
    def __call__(self,environ, start_response):
        path    = environ['PATH_INFO']
        method  = environ['REQUEST_METHOD']
        if method == 'POST':
            try:
                size = int(environ['CONTENT_LENGTH'])
                raw_string = environ['wsgi.input'].read(size)
            except (TypeError, ValueError):
                raw_string = ""
            try:
                query_string = str(raw_string)
            except:
                query_string = ""
            param = cgi.parse_qs(query_string)
            parameters = {}
            for k,v in param.items():
                parameters[k] = v.pop()
            return self.process(environ, start_response, parameters)
        if method == 'GET':
            query_string = environ['QUERY_STRING']
            param = cgi.parse_qs(query_string)
            parameters = {}
            for k,v in param.items():
                parameters[k] = v.pop()
            return self.process(environ, start_response, parameters)
            
    def process(self, environ, start_response, parameters):
        start_response('200 OK',[('Content-type', 'text/html')])
        response = "<p>---start---</p>"
        for k,v in parameters.items():
            response += "<p>%s = %s</p>" % (k,cgi.escape(v.pop()))
        response += "<p>---end---</p>"
        return [response]
        
#    def run(self,port):
#        httpd = make_server('',int(port),self)
#        print "Serving on port %s..." % port
#        httpd.serve_forever()


if __name__ == "__main__":        
    ws = WebServer()

