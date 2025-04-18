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

""" Pensando em um sistema do Uber: """

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None: 
        print('Carro popular está buscando o cliente...')

class Moto(Veiculo):
    def buscar_cliente(self):
        print('Moto está bucando cliente...')


class VeiculoFactory:
    @staticmethod
    def get_carro(tipo: str) -> Veiculo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        
        if tipo == 'luxo':
            return CarroLuxo()

        elif tipo == 'popular':
            return CarroPopular()

        elif tipo == 'moto':
            return Moto()

        assert 0, 'Carro não existe'


if __name__ == "__main__":
    from random import choice

    carros_disponiveis = ['luxo', 'popular', 'moto']

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()


 



