# Escopo da classe e de métodos da classe
class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} esta acabando com o {alimento}'

    def executar(self, *args,**kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome= 'Leão da tribo de judá')
print(leao.nome)
print(leao.executar('diabo'))



