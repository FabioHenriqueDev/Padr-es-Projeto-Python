def singleton(the_class):
    instance = {} # Dicionário onde vamos armazzzenar a instancia

    def get_class(*args, **kwargs):
        if the_class not in instance:
            instance[the_class] = the_class(*args, **kwargs)# instancia o objeto no theclass(*args, **kwargs)
            print(instance)
        return instance[the_class]
    

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        print('oi')
        self.tema = 'tema escuro'
        self.font_sie = '18px'
    

if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'tema claro'

    print(as1.tema)

    as2 = AppSettings()
    print(as2.tema)