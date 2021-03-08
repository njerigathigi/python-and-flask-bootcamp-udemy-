from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome!Go to /puppy_latin/name to see your name in puppy latin</h1>"

@app.route("/puppy_latin/<name>")
def puppy_latin(name):
    if name[-1] != "y":
        return "<h1> Hi {0}! Your puppy latin name is {1}.</h1>".format(name, name + "y")

    else:
        return "<h1> Hi {0}! Your puppy latin name is {1}.</h1>".format(name, name[0:len(name)-1] + "iful")


if __name__ == "__main__":
    app.run(debug=True)
