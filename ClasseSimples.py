class Pessoa:
    
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        
    def cadastro(self):
        return f'{self.__nome} {self.__cpf}'
    
    
p1 = Pessoa('Laika', 321456987)
p2 = Pessoa('Barba', 789654123)
p3 = Pessoa('Berruga', 456987123)

print(p1.cadastro())
print(p2.cadastro())
print(p3.cadastro())

        