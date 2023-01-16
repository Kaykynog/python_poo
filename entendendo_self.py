# Entendendo self em classes Phthon
# Classe - Molde (geralmente sem dados)
# Instância de class (objeto) - Tem os dados
# Uma classe pode gerarvárias instancias 

class Carro:
    def __init__(blabla, nome): # Pode ser qualquer nome
        blabla.nome = nome

    def acelerar(blabla):
        print(f'{blabla.nome} está acelerando...')


pegeout = Carro('pegeoutzin')
Carro.acelerar(pegeoutzin)
""" print(pegeout.nome)

pegeout.acelerar()

camaro = Carro(nome= 'Lambo')
print(camaro.nome)
camaro.acelerar() """ 