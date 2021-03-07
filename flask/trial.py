from flask import Flask

app = Flask(__name__)

@app.route("/") #127.0.0.1:5000
def cutecat():
    return "<h1>CuteCat</h1>"

@app.route("/whoarewe")
def whoarewe(): #127.0.0.1:5000/whoarewe
    return "<h1>We are ailurophile,</h1>"

@app.route("/cuteyprofile/<name>") #variable name passed into the route decorator will be synced to the one 
def cutey(name):                   #passed into the function ie they are the same.
    return "<h3>my name is {0} and i am cute.</h3>".format(name[200])


if __name__ == "__main__":
    app.run(debug=True)
