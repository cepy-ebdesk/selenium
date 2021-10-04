from flask import request
from gevent.pywsgi import WSGIServer

from api import API

app = API(__name__)


@app.route("/html")
def html():
    url = request.args.get('url')
    return app.html(url)


http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()
