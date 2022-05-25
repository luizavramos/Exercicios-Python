class Bola:
    def __init__(self, cor, circuferencia, material):
        self._cor = cor
        self._circunferencia = circuferencia
        self._material = material

    def troca_cor(self):
        return self._cor

    def troca_cor(self, cor):
        self._cor = cor

    def mostra_cor(self):
        return self._cor

    def mostra_atributos(self):
        return self._cor, self._circunferencia, self._material


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, lado):
        self.lado = lado

    def calcular_area(self, lado):
        self.area = int(lado) * int(lado)

    def mostrar_area(self):
        return self.area

    def mostrar_atributos(self):
        return self.lado

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        