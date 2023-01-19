# Metodos em instancias de classes Python 
# Hard coded - è algo que foi escrito diretamente no código
class Carro: 
    def __init__(self, nome) -> None: #metodo init sempre retorna None
        self.nome = nome 

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')

pegeout = Carro('pegeoutzin')
print(pegeout.nome)

pegeout.acelerar()

camaro = Carro(nome= 'Lambo')
print(camaro.nome)
camaro.acelerar()