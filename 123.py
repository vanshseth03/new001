from flask import Flask

app = Flask(__name__)

@app.route("/1111")
def index1():
    return "Hello World11111!"


@app.route("/ab")
def index():
    return "Hello World!vansh"

if __name__ ==  "__main__":
	app.run(debug=True)
