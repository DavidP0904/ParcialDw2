class PrestamoDecorador:
    def __init__(self, prestamo_envuelto):
        self.prestamo_envuelto = prestamo_envuelto

    @property
    def libro(self):
        return self.prestamo_envuelto.libro

    @property
    def dias_atraso(self):
        return self.prestamo_envuelto.dias_atraso

    @property
    def usuario(self):
        return self.prestamo_envuelto.usuario

    def calcular_multa(self):
        return self.prestamo_envuelto.calcular_multa()

    def __str__(self):
        return str(self.prestamo_envuelto)


class PrestamoConRenovacion(PrestamoDecorador):
    COSTO_RENOVACION = 4.0
    def calcular_multa(self):
        return self.prestamo_envuelto.calcular_multa() + self.COSTO_RENOVACION
    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo} ({self.libro.tipo()}) - {self.dias_atraso} días de atraso - Bs {self.calcular_multa()} (+ renovación)"


class PrestamoConEntregaDomicilio(PrestamoDecorador):
    COSTO_DOMICILIO = 6.0
    def calcular_multa(self):
        return self.prestamo_envuelto.calcular_multa() + self.COSTO_DOMICILIO
    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo} ({self.libro.tipo()}) - {self.dias_atraso} días de atraso - Bs {self.calcular_multa()} (+ entrega a domicilio)"