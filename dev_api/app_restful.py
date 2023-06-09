from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id' : '0',
        'nome': 'Rennan',
        'habilidades' : ['Python,', 'Django', 'Flask', 'SQL', 'HTML', 'CSS', 'JS']
    },

    {
    'id' : '1',
    'nome' : 'Augusto',
    'habilidades': ['Java', 'C#', 'C++']
    }
]

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status' : 'erro', 'mensagem' : 'Desenvolvedor de {} ID não existe '.format(id)}
        except Exception:
            mensagem = 'Erro desconhecido, procura o ADM da API'
            response = {'status' : 'erro', 'mensagem' : mensagem}
        return response
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self,id):
        desenvolvedores.pop(id)
        return {'stauts' : 'sucesso', 'mensagem' : 'Registro excluído'}

class listaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(listaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)