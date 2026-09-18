from libro import Libro

class LibroFisico(Libro):
    def tipo(self):
        return "Físico"

class LibroDigital(Libro):
    def tipo(self):
        return "Digital"