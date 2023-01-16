# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

string = 'kayky nogueira'
print(string.capitalize())

class Pessoa: 
    ...

p1 = Pessoa() # Criando instancia (Object)
print(p1)
p1.nome = 'kayky'
p1.sobrenome = 'nogueira'

p2 = Pessoa()
p2.nome = 'juan'
p2.sobrenome = 'nogueira'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
