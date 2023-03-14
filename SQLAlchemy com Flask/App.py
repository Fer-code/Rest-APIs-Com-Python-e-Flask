from flask import Flask, request
from flask_restful import Resource, Api
from Models import Pessoas, Atividades
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#dicionário de usuários
USUARIOS={
    'fernanda':'123',
    'julia':'908'
}

#método de autentificaçao
@auth.verify_password
def verificacao(login,senha):
    print("Validando usuário")
    print(USUARIOS.get(login)==senha)
    #se não informar ambas informações
    if not(login, senha):
        return False
    #else:
    return USUARIOS.get(login)==senha

#classes:
class Pessoa(Resource):
    @auth.login_required
    def get(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }
        except AttributeError:
            response={
                'status':'erro',
                'mensagem': 'Pessoa nao encontrada'
            }

        return response
    
    def put(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade= dados['idade']
        pessoa.save()

        response = {
            'id' : pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

    def delete(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
        pessoa.delete()
        return {'status':'ok', 'mensagem': mensagem}
    
#outra classe
class listar_pessoas(Resource):
    @auth.login_required
    def get(self):
        pessoas = Pessoas.query.all()
        #criando um dicionário a partir do 'for':
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade}for i in pessoas]
        return response
    
    def post(self):
        data = request.json
        pessoa = Pessoas(nome=data['nome'], idade=data['idade'])
        pessoa.save()
        response={
            'id':pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response
    
#classe de atividades
class atividade_lista(Resource):

    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.idativ, 'nome':i.nomeAtiv, 'pessoa': i.pessoa.nome} for i in atividades]
        return response


    def post(self):
        data = request.json
        pessoa = Pessoas.query.filter_by(nome=data['pessoa']).first()
        atividade = Atividades(nomeAtiv=data['nome'], pessoa = pessoa)
        atividade.save()

        response={
            'pessoa':atividade.pessoa.nome,
            'nome': atividade.nomeAtiv,
            'id':atividade.idativ
        }

        return response
    

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(listar_pessoas, '/pessoa/')
api.add_resource(atividade_lista, '/atividade/')


if __name__ == '__main__':
    app.run(debug=True)