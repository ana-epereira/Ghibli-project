from flask import Flask
import pandas as pd

df = pd.read_csv('Ghibli characters.csv')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Teste'

@app.route('/about')
def about():
    return 'About'

