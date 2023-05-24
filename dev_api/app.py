from flask import Flask, jsonify, request
import json
app = Flask(__name__)

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

@app.route('/dev/<int:id>/', methods=['GET', 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status' : 'erro', 'mensagem' : 'Desenvolvedor de {} ID não existe '.format(id)}
        except Exception:
            mensagem = 'Erro desconhecido, procura o ADM da API'
            response = {'status' : 'erro', 'mensagem' : mensagem}

        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'stauts' : 'sucesso', 'mensagem' : 'Registro excluído'})



@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({desenvolvedores[posicao]})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)




if __name__ == '__main__':
    app.run()