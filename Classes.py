class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    
p1 = Pessoa('andre', 'freitas')

print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa('laika', 'berruga')

print(p2.nome)
print(p2.sobrenome)