import time


def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f'Sua função demorou, {tempo_final - tempo_inicial} para ser executada')
    
    return wrapper



@calcular_tempo
def contar_ate_100000():
    for n in range(10000 + 1):
        print(n)


contar_ate_100000()



