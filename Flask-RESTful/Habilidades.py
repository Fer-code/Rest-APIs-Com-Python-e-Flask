from flask_restful import Resource
from flask import Flask,  request
import json

listahabilidades = [{'nome': 'Python'}, {'nome': 'Java'}, {'nome':'Flask'}, {'nome':'PHP'}]

#get e post
class Habilidade(Resource):
    def get(self):
        return listahabilidades
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(listahabilidades)
        dados['id'] = posicao
        listahabilidades.append(dados)
        return {'status':'ok', 'mensagem':'Habilidade Inserido com sucesso'}
    
#put e delete
class Habi_put_delete(Resource):
    def put(self,id):
        dados = json.loads(request.data)
        listahabilidades[id] = dados
        return {'status ok'}
    
    def delete(self,id):
        listahabilidades.pop(id)
        return {'status':'sucesso', 'mensagem': 'registro excluido'}