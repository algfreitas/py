class Pessoa:
    ano_atual = 2022   
        
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade    
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('laika', 9)
p1.__dict__['peso'] = 35
print(p1.__dict__) 