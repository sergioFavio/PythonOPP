class Cliente:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    @property
    def nombre(self):
        print('llamando a @property nombre()')
        return self.__nombre.title()
        