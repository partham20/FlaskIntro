from flask import Flask


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "Hello"

@app.route("/greet/<name>")
def name(name):
    return "Hello "+name

if __name__=="__main__":
    app.run(debug=True,port=5001)