

def validar(function):
    def valida(x, y):
        if x< 0 or y < 0:
            raise ValueError('X e Y não podem sern gativos')
        
        return function(x, y)
    
    return valida
    

@validar
def soma(x, y):
    return x + y

print(soma(10, 10))

