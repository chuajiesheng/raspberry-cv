#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        try:
            #Check the file extension required and
            #set the right mime type

            print 'Serve:', self.path

            sendReply = False
            if self.path.endswith(".png"):
                mimetype='image/png'
                sendReply = True

            if sendReply == True:
                #Open the static file requested and send it

                file = '/home/exer/workspace/raspberry-cv/basic-capture' + sep + self.path
                print 'Serve', file

                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                f = open(file)
                self.wfile.write(f.read())
                f.close()
            return


        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

def main():
    print 'Started main'
    try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        #Wait forever for incoming http requests
        server.serve_forever()
        print 'Started httpserver on port' , PORT_NUMBER

    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()

if __name__ == "__main__":
    print 'Started'
    main()
