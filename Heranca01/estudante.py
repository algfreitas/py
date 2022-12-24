from pessoa import Pessoa

class Estudante(Pessoa):    
    def __init__(self, nome, cpf, matricula):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        
    def get_estudante(self):
        return f'{self.__matricula}'
    

        