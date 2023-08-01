from flask import Flask, render_template, request, abort, redirect, url_for
import json, sys
from ampq.tasker import Tasker
from readers.dataExcelRW import DataExcelRW

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST','GET'])
def menu():
    # return render_template('index.html')
    return;

@app.route('/cadastro', methods=['POST','GET'])
def cadastro():
    if request.method == 'POST':
       googleExcelId = request.form.get('googleExcelId')
    elif request.method == 'GET':
        googleExcelId = request.args.get('googleExcelId')


    #mensageria
    task_insert = Tasker('pet')
    task_insert.send('loadGoogleExcel', googleExcelId)
    return f'dado(s) do Google Excel de Id: {googleExcelId} enviado(s) para cadastro'

@app.route('/mongo2postgres', methods=['POST','GET'])
def listar():
    if request.method == 'POST':
        # return request.form.to_dict()
        task_get = Tasker('pet')
        return "objetos listados na fila"
       #colocar o serviço de mensageria para buscar o array de json
    else:
        abort(403) #status 403 = proibido

@app.route('/actions', methods=['POST','GET'])
def actions():
    if request.method == 'POST':
        return render_template('actions.html', matricula=request.form.to_dict()["matricula"])
        # return request.form.to_dict()["matricula"]
       #colocar o serviço de mensageria para buscar o array de json
    else:
        abort(403) #status 403 = proibido

@app.route('/delete', methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        return "usuario deletado"
        # return request.form.to_dict()["matricula"]
       #colocar o serviço de mensageria para buscar o array de json
    else:
        abort(403) #status 403 = proibido

if __name__ == '__main__':
    app.run(debug=True)