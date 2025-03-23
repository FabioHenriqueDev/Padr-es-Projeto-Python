"""📌 O que é uma metaclasse?
Uma metaclasse é como uma "fábrica de classes".
➡ Enquanto classes criam objetos, metaclasses criam classes.
"""

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]



class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'tema escuro'
        self.font_sie = '18px'
    

if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()
    as3 = AppSettings()

    as1.tema = 'tema claro'

    print(as3.tema)
