def notificar_biblioteca(prestamo):
    print(f"  [biblioteca] Registrar préstamo: {prestamo.libro.titulo}")

def notificar_usuario(prestamo):
    print(f"  [usuario] Aviso a {prestamo.usuario}: multa acumulada Bs {prestamo.calcular_multa()}")