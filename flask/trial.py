from flask import Flask

app = Flask(__name__)

@app.route("/") #127.0.0.1:5000
def cutecat():
    return "<h1>CuteCat</h1>"

@app.route("/whoarewe")
def whoarewe(): #127.0.0.1:5000/whoarewe
    return "<h1>We are aureolophiles</h1>"

@app.route("/cuteyprofile/<name>") #variable name passed into the route decorator will be synced to the one 
def cutey(name):                   #passed into the function ie they are the same.
    return "<p>my name is {0}</p>".format(name)


if __name__ == "__main__":
    app.run()
