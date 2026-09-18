from gestor_prestamos import GestorPrestamos
from prestamo import Prestamo
from prestamo_decorador import PrestamoConRenovacion, PrestamoConEntregaDomicilio
from notificaciones import notificar_biblioteca, notificar_usuario
from canales_prestamo import catalogar_mostrador, catalogar_en_linea

gestor = GestorPrestamos()
gestor.suscribir(notificar_biblioteca)
gestor.suscribir(notificar_usuario)

libro1 = catalogar_mostrador("Físico", "Cien años de soledad", 2.0)
libro2 = catalogar_en_linea("Digital", "1984", 1.0)

p1 = Prestamo(libro1, 5, usuario="Marco")
p2 = PrestamoConRenovacion(Prestamo(libro2, 3, usuario="Sofia"))
p3 = PrestamoConEntregaDomicilio(Prestamo(libro1, 2, usuario="Elena"))

print("Registrando préstamos...")
gestor.registrar(p1)
gestor.registrar(p2)
gestor.registrar(p3)

print("\nListado de préstamos:")
for p in gestor.prestamos:
    print(" ", p)

print("\nTotal de multas:", gestor.total_multas())