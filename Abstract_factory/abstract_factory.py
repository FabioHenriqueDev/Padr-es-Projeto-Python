"""
O Abstract Factory é um padrão de criação que fornece uma interface para criar famílias de objetos relacionados ou dependentes, sem especificar suas classes concretas. Normalmente, ele utiliza um ou mais Factory Methods para instanciar esses objetos.

Uma diferença essencial entre Factory Method e Abstract Factory é que o Factory Method utiliza herança, enquanto o Abstract Factory se baseia na composição.

📌 Princípio: Programe para interfaces, não para implementações.
"""

""" Pensando em um sistema do Taxi: """

from abc import ABC, abstractclassmethod

class VeiculoLuxo(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None: pass

class VeiculoPopular(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None: pass


# Zona Norte:

class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None: 
        print('Carro de luxo ZN está buscando o cliente...')

class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None: 
        print('Carro popular ZN está buscando o cliente...')

class MotoLuxoZN(VeiculoLuxo):
      def buscar_cliente(self):
        print('Moto de luxo ZN está bucando cliente...')

class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self):
        print('Moto popular ZN está bucando cliente...')


# Zona leste:

class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None: 
        print('Carro de luxo ZS está buscando o cliente...')

class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None: 
        print('Carro popular ZS está buscando o cliente...')

class MotoLuxoZS(VeiculoLuxo):
      def buscar_cliente(self):
        print('Moto de luxo ZS está bucando cliente...')

class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self):
        print('Moto popular ZS está bucando cliente...')




class VeiculoFactory(ABC):
    @staticmethod
    @abstractclassmethod
    def get_carro_luxo() -> VeiculoLuxo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        pass
    
    @staticmethod
    @abstractclassmethod
    def get_carro_popular() -> VeiculoPopular: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        pass
    
    @staticmethod
    @abstractclassmethod
    def get_moto_luxo() -> VeiculoLuxo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        pass

    @staticmethod
    @abstractclassmethod
    def get_moto_popular() -> VeiculoPopular: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        pass




class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        return CarroLuxoZN()
    
    @staticmethod
    def get_carro_popular() -> VeiculoPopular: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        return CarroPopularZN()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        return MotoPopularZN()



class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        return CarroLuxoZS()
    
    @staticmethod
    def get_carro_popular() -> VeiculoPopular: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        return CarroPopularZS()
    
    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular: # Esse é um metodo fabrica, basicamente um método que cria os objetos
        return MotoPopularZS()


class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()
            
            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()

            print(69 * '-')





if __name__ == "__main__":
   cliente = Cliente()
   cliente.busca_clientes()

 



