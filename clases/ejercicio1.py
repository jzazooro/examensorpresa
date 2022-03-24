class libro():
    def __init__(self, titulo, autor, editorial, isbn, fechadepublicacion):
        self.titulo=titulo
        self.autor=autor
        self.editorial=editorial
        self.isbn=isbn
        self.fechadepublicacion=fechadepublicacion
    def libro(self):
        print("se trata del libro", self.titulo, "del autor", self.autor, "de la editorial", self.editorial, "con isbn", self.isbn, "que se publico el dia", self.fechadepublicacion)
busqueda=libro("cancion de hielo y fuego", "George R R Martin", "Gigamesh", "F4J7VN49", "1 de agosto de 1996")
busqueda.libro()