#!/usr/bin/env python3

from flask import Flask






#flask ctor takes the name mod as arg
app = Flask(__name__)




#the path that flask will send get request
@app.route("/")
def hello_world():
    return "Hello World"

if __name__ == " __main__":
    app.run(host="0.0.0.0", port=2224)

