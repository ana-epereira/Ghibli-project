from flask import Flask, render_template
from pandas import pandas

app = Flask(__name__,template_folder="template")

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)

