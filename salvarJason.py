import json

arquivo_dados = 'arquivo_dados.json'

class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        

       
p1 = Pessoa('berruga', 98563247815) 
print(p1.nome, p1.cpf)

p2 = Pessoa('barba', 52459685665) 
print(p2.nome, p2.cpf)

p3 = Pessoa('laika', 42123658996) 
print(p3.nome, p3.cpf)

# Utilizando __dict e ou vars, mesmo resultado.
dados = [p1.__dict__, p2.__dict__, vars(p3)]

with open(arquivo_dados, 'w') as arquivo_dados:
    json.dump(dados, arquivo_dados, ensure_ascii=False, indent=2)


  
  
        
        