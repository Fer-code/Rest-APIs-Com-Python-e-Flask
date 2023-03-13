from flask import Flask, jsonify , request
import json
app = Flask(__name__)

desenvolvedores = [
    {'id':'0',
     'nome':'Fernanda',
     'habilidades': ['java', 'python']},

    {'id':'1',
     'nome':'Henrique',
     'habilidades': ['C#']}
]

@app.route('/dev/<int:id>/', methods=['GET','PUT', 'DELETE']) #tipagem
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem': 'Desenvolvedor de ID {} não existe.'.format(id)}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify({'status ok'})
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem': 'registro excluido'})
    
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify ({'status':'ok', 'mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == "__main__" :
    app.run(debug=True)