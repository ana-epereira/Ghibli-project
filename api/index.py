from flask import Flask, render_template
from pandas import pandas as pd

app = Flask(__name__,template_folder="template")

df = pd.read_csv("Ghibli characters.csv")
antigo = df['movie'][df['release date'] == df['release date'].min()].drop_duplicates().to_string()
antigo = antigo[2:]
ano1 =  df['release date'][df['release date'] == df['release date'].min()].drop_duplicates().to_string()
ano1 = ano1[2:]

@app.route("/")
def home():
    return render_template("home.html",antigo = antigo,ano1=ano1)

    
if __name__ == "__main__":
    app.run(debug=True)

