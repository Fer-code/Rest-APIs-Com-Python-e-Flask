from Models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Gabriela', idade=27)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    print(pessoa)

    #filtrar
    filtro = Pessoas.query.filter_by(nome='Gabriela').first()
    print('Filtro idade:  {}'.format(filtro.idade))

def alterar():
    pessoa = input("Digite o nome da pessoa para alteração:")
    filtro = Pessoas.query.filter_by(nome=pessoa).first()
    
    idade = int(input("Insira a nova idade:"))
    filtro.idade = idade
    filtro.save()

def excluir():
    pessoa = input('nome da pessoa que deseja excluir: ')
    exclusao = Pessoas.query.filter_by(nome=pessoa).first()
    exclusao.delete()

if __name__ == '__main__':
    #insere_pessoas()
    excluir()
    consulta()
    #alterar()