from flask_restful import Resource

habilidades = ['Python', 'Java', 'C#']
class Habilidades(Resource):
    def get(self):
        return habilidades