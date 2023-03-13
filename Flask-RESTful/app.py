from flask import Flask,  request
from flask_restful import Resource, Api
import json
from Habilidades import Habilidade, Habi_put_delete


app = Flask(__name__)
api = Api(app)

#lista desenvolvedores
desenvolvedores = [
    {'id':'0',
     'nome':'Fernanda',
     'habilidades': ['java', 'python']},

    {'id':'1',
     'nome':'Henrique',
     'habilidades': ['C#']}
]

#criar uma classe
class Desenvolvedor(Resource):

    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status':'erro', 'mensagem': 'Desenvolvedor de ID {} não existe.'.format(id)}
        return response
    
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return {'status ok'}

    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem': 'registro excluido'}
    
#criar outra classe
class Listar_acrescentar_dev(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)

        return {'status':'ok', 'mensagem':'Inserido com sucesso'}

#definir rota
api.add_resource(Desenvolvedor, '/dev/<int:id>/')

#definir rota de listar e post
api.add_resource(Listar_acrescentar_dev, '/dev/')

#definir rota habilidades
api.add_resource(Habilidade, '/habilidade/')

#definir rota habilidades: delete e put
api.add_resource(Habi_put_delete, '/habilidade/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)

