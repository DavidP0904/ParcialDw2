class GestorPrestamos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.prestamos = []
            cls._instancia.observadores = []
        return cls._instancia

    def suscribir(self, funcion_observadora):
        self.observadores.append(funcion_observadora)

    def _notificar(self, prestamo):
        for funcion in self.observadores:
            funcion(prestamo)

    def registrar(self, prestamo):
        self.prestamos.append(prestamo)
        self._notificar(prestamo)

    def total_multas(self):
        return sum(p.calcular_multa() for p in self.prestamos)