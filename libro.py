from abc import ABC, abstractmethod

class Libro(ABC):
    def __init__(self, titulo, multa_diaria):
        self.titulo = titulo
        self.__multa_diaria = multa_diaria

    @property
    def multa_diaria(self):
        return self.__multa_diaria

    @multa_diaria.setter
    def multa_diaria(self, nueva_multa):
        if nueva_multa < 0:
            raise ValueError("La multa diaria no puede ser negativa")
        self.__multa_diaria = nueva_multa

    @abstractmethod
    def tipo(self):
        pass

    def __str__(self):
        return f"{self.titulo} ({self.tipo()})"