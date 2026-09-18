from fabrica_libros import FabricaLibros

def catalogar_mostrador(tipo, titulo, multa_diaria):
    return FabricaLibros.crear(tipo, titulo, multa_diaria)

def catalogar_en_linea(tipo, titulo, multa_diaria):
    return FabricaLibros.crear(tipo, titulo, multa_diaria)