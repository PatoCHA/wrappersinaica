import logging
import sys
import os
from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import requests
from bs4 import BeautifulSoup
from pandas.io.json import json_normalize
import json
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'bienvenido'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/estacion/<articleid>')
def api_article(articleid):
    url='http://sinaica.inecc.gob.mx/pags/datGrafs.php'
    params ={'estacionId':str(articleid),'param':'NO','fechaIni':'2017-03-01','rango':'4','tipoDatos':''}

    response=requests.post(url, data=params)
    soup1 = BeautifulSoup(response.text, 'lxml')
    reportes = soup1.find_all('script')[2]
    r = str(reportes)
    r1 = r.split(' dat = ')
    r2 = r1[1].rsplit(';\n\n\t\tif(dat.length == 0)')
    r3 = r2[0].rsplit("['(.*?)']")
    JsonText=r3[0].decode('utf-8')
    new =json.loads(JsonText)# This line performs query and returns json result
    return jsonify(new={"status": 200})
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
