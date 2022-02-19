class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def exibe_nome_e_sobrenome(self):
        print("{} {}".format(self.nome, self.sobrenome))


#from pessoa import Pessoa
#pessoa = Pessoa("Tamiris", "Coutinho")
#pessoa.exibe_nome_e_sobrenome()
 
