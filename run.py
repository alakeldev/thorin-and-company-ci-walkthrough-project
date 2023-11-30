import os
from flask import Flask   # Import Flask Class

app = Flask(__name__)    # Creating Instance and store it inside variable called app ====>>>>>>the first argument of the flask class is the name of application module

@app.route("/")    # Decorator app.route  decorator to wrapping functions
def index():
    return "Hello, World"




if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)   # you should know that you shoud neve have debug=True when you want to submit your project to assesment or even in production application