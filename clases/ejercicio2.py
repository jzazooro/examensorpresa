class animal(self, tipo):
    def __init__(self, tipo):
        self.tipo=tipo

class mamifero(animal):
    def __init__(self, tipo, mamifero):
        super().__init__(tipo)

        self.mamifero=mamifero
class oviparo(mamifero):
    def __init__(self, tipo, mamifero, oviparo):
        super().__init__(tipo, mamifero)
        self.oviparo=oviparo
        
pollo=animal("pollo")
gato=mamifero("gato", True)
ornitorrinco=oviparo("ornitorrinco", True, True)
print(ornitorrinco.mamifero)