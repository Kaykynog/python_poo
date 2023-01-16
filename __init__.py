class Pessoa():
    def __init__(self, nome, sobrenome): # Método __init__
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Luiz', 'Paulo')

p2 = Pessoa('Kayky', 'Nogueira')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome) 
print(p2.sobrenome)
 