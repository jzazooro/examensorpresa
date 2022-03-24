class animal(self, tipo):
    def __init__(self, tipo):
        self.tipo=tipo
class mamifero(animal):
    def __init__(self, tipo, mamifero):
        super().__init__(tipo)
        self.mamifero=mamifero
class oviparo(mamifero):
    def __init__(self, tipo, mamifero, oviparo):
