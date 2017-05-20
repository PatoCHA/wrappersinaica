import logging #ver mejor los errores
import sys #ver mejor los errores
import os #sirve para usar el puerto abierto en heroku
from flask import Flask, request 
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
import requests
from bs4 import BeautifulSoup
from pandas.io.json import json_normalize
import json
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Bienvenido, https://github.com/PatoCHA/wrappersinaica'

@app.route('/estacion', methods=['GET'])
def api_article():
    estacion = request.args.get('estacion') 
    fecha = request.args.get('Fecha')
    rango= request.args.get('rango')
    conta = request.args.get('parametro')
    url='http://sinaica.inecc.gob.mx/pags/datGrafs.php'
    params ={'estacionId':str(estacion),'param':str(conta),'fechaIni':str(fecha),'rango':str(rango),'tipoDatos':''}

    response=requests.post(url, data=params)
    soup1 = BeautifulSoup(response.text, 'lxml')
    reportes = soup1.find_all('script')[2]
    r = str(reportes)
    r1 = r.split(' dat = ') #extraccion de datos
    r2 = r1[1].rsplit(';\n\n\t\tif(dat.length == 0)') #extraccion de datos
    r3 = r2[0].rsplit("['(.*?)']") #extraccion de datos
    JsonText=r3[0].decode('utf-8') #extraccion de datos
    new =json.loads(JsonText)   # regresa un json
    return jsonify(new) #respuesta

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

#brindan mas informacion sobre los errores
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
