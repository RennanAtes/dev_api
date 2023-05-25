from models import Pessoas, db_session


def insere_pessoas():
    pessoa = Pessoas(nome='Rennan', idade='19')
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.filter_by(nome='Rennan')
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Augusto')
    print(pessoa)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Galleani').first()
    pessoa.idade = 20
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe')
    pessoa.delete()




if __name__ == '__main__':
    insere_pessoas()
    consulta()