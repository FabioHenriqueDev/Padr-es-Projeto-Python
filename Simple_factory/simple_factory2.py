"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a fábrica pode retornar um objeto já criado para o cliente, ao invés de criar novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado  
Simple Factory pode não ser considerado um padrão de projeto por si só  
Simple Factory pode quebrar princípios do SOLID  
"""

""" Pensando em um sistema do Taxi: """

from abc import ABC, abstractclassmethod

class Veiculo(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Carro popular está buscando o cliente...')

class Moto(Veiculo):
    def buscar_cliente(self):
        print('Moto popular está bucando cliente...')

class MotoLuxo(Veiculo):
      def buscar_cliente(self):
        print('Moto de luxo está bucando cliente...')


class VeiculoFactory(ABC):

    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractclassmethod
    def get_carro(tipo: str) -> Veiculo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        
        if tipo == 'carro de luxo':
            return CarroLuxo()

        elif tipo == 'carro popular':
            return CarroPopular()

        elif tipo == 'moto popular':
            return Moto()

        elif tipo == 'moto de luxo':
            return MotoLuxo()

        assert 0, 'Carro não existe'


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        
        if tipo == 'carro de luxo':
            return CarroLuxo()

        elif tipo == 'carro popular':
            return CarroPopular()

        elif tipo == 'moto popular':
            return Moto()
        
        elif tipo == 'moto de luxo':
            return MotoLuxo()

        assert 0, 'Carro não existe'



if __name__ == "__main__":
    from random import choice

    veiculos_disponiveis_zona_norte = ['carro de luxo', 'carro popular', 'moto popular', 'moto de luxo']
    veiculos_disponiveis_zona_sul = ['carro popular', 'moto popular']

    print('Zona Norte: ')
    print()
    
    for i in range(3):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()
    
    print('--' * 68)
    print()

    print('Zona Sul:')
    print()
    for i in range(3):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()


 



