from flask import Flask, render_template, url_for

app  = Flask(__name__)

@app.route("/")
def karibu():
    return '<h1 style="font-family:cursive;font-style:italic;">welcome! Meow!</h1>'

@app.route("/meow")
def about():
    return render_template("index.html") #html file has to be in a templates folder at the same level as your .py file.

if __name__ == "__main__":
    app.run(debug=True)
