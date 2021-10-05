from flask import request
from gevent.pywsgi import WSGIServer

from api import API

app = API(__name__)


@app.route("/html")
def html():
    url = request.args.get('url')
    wait_for_el = request.args.get('wait_for_el')
    return app.html(url, wait_for_el)


http_server = WSGIServer(('0.0.0.0', 5000), app)
http_server.serve_forever()
