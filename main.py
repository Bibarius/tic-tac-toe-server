from http.server import *
import json
from urllib.parse import parse_qs
import os
import game

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path[1:]
        if not path:
            f = open("frontend/index.html", "rb")
            File = f.read()
            self.send_response(200)
            self.send_header('Content-Lenth', str(len(File)))
            self.end_headers()
            self.wfile.write(File)

        elif path[:5] == 'solve':
            data = parse_qs(self.path)['/solve*?data'][0]
            jdata = json.loads(data)
            field = jdata['field']
            move = jdata['move']

            print('field = ', field)
            print('move = ', move)


            #!TODO ЗДЕСЬ БУДЕТ ИДТИ РЕШЕНИЕ ДОСКИ И ОТПРАВКА НАЗАД
            


        else:
            try:                
                f = open('frontend/' + path, 'rb')
            except FileNotFoundError:
                print(path)
                print('requested file ' + path + ' wasnt found on server')
                return 1
            
            print(self.client_address)

            File = f.read()
            self.send_response(200)

            if path.find('css'):
                self.send_header('Content-Type', 'text/css')

            self.send_header('Content-Lenth', str(len(File)))
            self.end_headers()
            self.wfile.write(File)




if __name__ == "__main__":
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
    