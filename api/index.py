from flask import Flask,request, redirect, url_for
from io import TextIOWrapper
from flask_sqlalchemy import SQLAlchemy
#from pandas import pandas

app = Flask(__name__)

@app.route('/')
def home():
    return 'Teste'

@app.route('/', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        csv_file = request.files['file']
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            user = User(username=row[0], email=row[1])
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('upload_csv'))
    return """
            <form method='post' action='/' enctype='multipart/form-data'>
              Upload a csv file: <input type='file' name='file'>
              <input type='submit' value='Upload'>
            </form>
           """

@app.route('/ghibli')
def antigo():
    df = pandas.read_csv('Ghibli characters.csv')
    antigo = df['movie'][df['release date'] == df['release date'].min()].drop_duplicates().to_string()
    antigo = antigo[2:]
    return 'O filme mais antigo é {antigo}'

@app.route('/about')
def about():
    return 'About'

