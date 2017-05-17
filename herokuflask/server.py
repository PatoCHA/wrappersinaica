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
from flask import request as request1
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Bienvenido, Porfavor revisa la documentacion en github'

@app.route('/estacion', methods=['GET'])
def api_article():
    username = request1.args.get('estacion')
    fecha = request1.args.get('Fecha')
    rango= request1.args.get('rango')
    conta = request1.args.get('parametro')
    url='http://sinaica.inecc.gob.mx/pags/datGrafs.php'
    params ={'estacionId':str(username),'param':str(conta),'fechaIni':str(fecha),'rango':str(rango),'tipoDatos':''}

    response=requests.post(url, data=params)
    soup1 = BeautifulSoup(response.text, 'lxml')
    reportes = soup1.find_all('script')[2]
    r = str(reportes)
    r1 = r.split(' dat = ')
    r2 = r1[1].rsplit(';\n\n\t\tif(dat.length == 0)')
    r3 = r2[0].rsplit("['(.*?)']")
    JsonText=r3[0].decode('utf-8')
    new =json.loads(JsonText)# This line performs query and returns json result
    return jsonify(new)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
