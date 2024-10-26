import math

class FiguraGeometrica:
    def __init__(self, color_fondo: str, color_borde: str):
        self.color_fondo = color_fondo
        self.color_borde = color_borde
    
    def area(self) -> float:
        raise NotImplementedError("Debe implementar el método 'area' en la subclase")
    
    def perimetro(self) -> float:
        raise NotImplementedError("Debe implementar el método 'perimetro' en la subclase")

class Rectangulo(FiguraGeometrica):
    def __init__(self, color_fondo: str, color_borde: str, base: float, altura: float):
        super().__init__(color_fondo, color_borde)
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        return self.base * self.altura
    
    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

class Circulo(FiguraGeometrica):
    def __init__(self, color_fondo: str, color_borde: str, radio: float):
        super().__init__(color_fondo, color_borde)
        self.radio = radio
    
    def area(self) -> float:
        return math.pi * self.radio ** 2
    
    def perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Triangulo(FiguraGeometrica):
    def __init__(self, color_fondo: str, color_borde: str, base: float, altura: float):
        super().__init__(color_fondo, color_borde)
        self.base = base
        self.altura = altura
    
    def area(self) -> float:
        return (self.base * self.altura) / 2
    
    def perimetro(self) -> float:
        return 3 * self.base

# ejemploss
rectangulo = Rectangulo("rojo", "negro", 5.0, 3.0)
print("Área del rectángulo:", rectangulo.area())
print("Perímetro del rectángulo:", rectangulo.perimetro())

circulo = Circulo("azul", "blanco", 4.0)
print("Área del círculo:", circulo.area())
print("Perímetro del círculo:", circulo.perimetro())

triangulo = Triangulo("verde", "amarillo", 3.0, 4.0)
print("Área del triángulo:", triangulo.area())
print("Perímetro del triángulo (equilátero):", triangulo.perimetro())