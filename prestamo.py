class Prestamo:
    def __init__(self, libro, dias_atraso, usuario):
        self.libro = libro
        self.dias_atraso = dias_atraso
        self.usuario = usuario

    def calcular_multa(self):
        return self.libro.multa_diaria * self.dias_atraso

    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo} ({self.libro.tipo()}) - {self.dias_atraso} días de atraso - Bs {self.calcular_multa()}"