from flask import Flask
from pandas import pandas

app = Flask(__name__)

@app.route('/')
def home():
    return 'Teste'

@app.route('/')
def antigo():
    df = pandas.read_csv('Ghibli characters.csv')
    antigo = df['movie'][df['release date'] == df['release date'].min()].drop_duplicates().to_string()
    antigo = antigo[2:]
    return 'O filme mais antigo é {antigo}'

@app.route('/about')
def about():
    return 'About'

