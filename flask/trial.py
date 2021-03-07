from flask import Flask

app = Flask(__name__)

@app.route("/") #127.0.0.1:5000

def cutecat():
    return "<h1>CuteCat</h1>"

@app.route("/whoarewe")

def whoarewe(): #127.0.0.1:5000/whoarewe
    return "<h1>We are aureolophiles</h1>"


if __name__ == "__main__":
    app.run()
