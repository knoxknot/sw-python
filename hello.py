import os,logging
from flask import Flask

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def hello():
  logging.debug("saying hello")
  name = os.environ.get("NAME", "Samuel")
  return "Hello %s" %name