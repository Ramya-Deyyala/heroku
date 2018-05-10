import os
import http.server
import requests
from urllib.parse import unquote, parse_qs
from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def HelloWorld():
   return "Hello Flask"

if __name__ == '__main__':
	port = int(os.environ.get('PORT',8000))
	server_address = ('', port)
	httpd = http.server.HTTPServer(server_address, Shortener)
	httpd.serve_forever()
	app.debug = True
	app.run(host='0.0.0.0', port=5000)

   