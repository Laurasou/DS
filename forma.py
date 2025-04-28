class Forma:
    def __init__(self,nome):
        self.nome = nome

    def calcula_Area(self):
        raise NotImplementedError("o método deve ser implementado em subclasse")

    def calcula_Perimetro(self):
        raise NotImplementedError("o método deve ser implementado em subclasse")

    def __str__(self):
        return f"Nome da forma geometrica = {self.nome}" 