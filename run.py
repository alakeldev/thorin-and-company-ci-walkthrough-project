import os
from flask import Flask, render_template   # Import Flask Class and render_template function

app = Flask(__name__)    # Creating Instance and store it inside variable called app ====>>>>>>the first argument of the flask class is the name of application module

@app.route("/")    # Decorator app.route  decorator to wrapping functions
def index():
    return render_template("index.html")
                        #"Hello, World"     # also you can put html elements here ex: "<h1>Hello, </h1><h2>World</h2>" instead of "Hello, World"


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)   # you should know that you shoud neve have debug=True when you want to submit your project to assesment or even in production application