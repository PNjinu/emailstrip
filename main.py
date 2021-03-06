from flask import Flask, redirect, url_for, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        string = request.form["string"]
        findEmail = re.findall('[\w\.-]+@[\w\.-]+', string)
        return render_template("index.html", content=findEmail)
    else:
        return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)