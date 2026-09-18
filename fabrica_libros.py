from libros_especificos import LibroFisico, LibroDigital

class FabricaLibros:
    @staticmethod
    def crear(tipo, titulo, multa_diaria):
        if tipo == "Físico":
            return LibroFisico(titulo, multa_diaria)
        elif tipo == "Digital":
            return LibroDigital(titulo, multa_diaria)
        else:
            raise ValueError(f"Tipo desconocido: {tipo}")