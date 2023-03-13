from flask import Flask, jsonify , request
import json
app = Flask(__name__)

# o 'jsonify' permite que retorne um formato JSON quando for chamado, o que é necessario para funcionar o 'return' abaixo

@app.route('/<int:id>') #tipagem
def pessoa(id):
    return jsonify({'id':id,'nome':'Jossef','profissao':'Engenheiro','Cor favorita':'Prata'})

@app.route('/soma/<int:v1>/<int:v2>')
def soma(v1,v2):
    return jsonify({'soma':v1+v2}) 

@app.route('/numeros', methods=['POST','GET'])
def soma2():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 10 + 20 + 400
    return jsonify({'soma': total})

if __name__ == "__main__" :
    app.run(debug=True)
