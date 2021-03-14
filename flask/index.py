from flask import Flask, render_template, url_for

app  = Flask(__name__)

@app.route("/")
def karibu():
    return '<h1 style="font-family:cursive;font-style:italic;">welcome! Meow!</h1>'

@app.route("/meow")
def about():
    cat1= "Nala"
    cat2="Sarabi"
    return render_template("index.html", pussycat=cat1, pussycat2=cat2) #html file has to be in a templates folder at the same level as your .py file.

@app.route("/mylikes/<name>")
def mylikes(name):
    jina = name
    return render_template("index.html", jina=jina)


if __name__ == "__main__":
    app.run(debug=True)
