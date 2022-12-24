class Pessoa:
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        
    def get_pessoa(self):
        return f'{self.__nome} {self.__cpf}'
          