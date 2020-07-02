
from flask import Flask,render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_cors import CORS

import pandas as pd
import os
import requests
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
CORS(app)

print(os.environ['APP_SETTINGS'])


@app.route('/api/rfzo-lista')
def return_data():
    df_fromsql = pd.read_sql_table('centops', db.session.bind)
    df_fromsql.rename(columns={'ustanova':'Ustanova', 'intervencija':'Intervencija', 'cekanje':'Čekanje', 'datum':'Datum', 'broj':'Broj', 'rok':'Rok'}, inplace=True)
    return jsonify(df_fromsql.to_dict(orient='records'))

if __name__ == '__main__':
    app.run()
