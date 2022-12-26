class Pessoa:
    ano_atual = 2022   
        
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade    
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('laika', 9)
print(p1.get_ano_nascimento())
p2 = Pessoa('barba', 8)
print(p2.get_ano_nascimento())
p3 = Pessoa ('andre', 46)
print(p3.get_ano_nascimento())    