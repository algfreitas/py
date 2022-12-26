class Animal:
    def __init__(self, nome):
        self.nome = nome
        
        
    def comendo(self, alimento):
        return f'{self.nome} esta comendo {alimento}'
    
        
a1 = Animal(nome='leao')
print(a1.nome)
print(a1.comendo('Bebe foca'))