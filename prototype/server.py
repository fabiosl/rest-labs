import urllib2
from flask import Flask, Response

app = Flask(__name__)

@app.route("/clientes")
def clients():
    xmlUrl = "file:///vagrant/prototype/resources/clientes.xml"
    xmlResouce = urllib2.urlopen(xmlUrl)
    return Response(xmlResouce, mimetype="text/xml")

@app.route("/")
def index():
    return Response("Hello Flask!", mimetype="text/html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
