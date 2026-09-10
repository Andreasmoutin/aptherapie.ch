from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/a-propos")
def a_propos():
    return render_template("a_propos.html")

@app.route("/accompagnements")
def accompagnements():
    return render_template("accompagnements.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)