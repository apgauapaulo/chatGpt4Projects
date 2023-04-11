import math

class Circulo:
def init(self, raio):
self.raio = raio

def area(self):
    return math.pi * self.raio ** 2

def perimetro(self):
    return 2 * math.pi * self.raio

class Retangulo:
def init(self, largura, altura):
self.largura = largura
self.altura = altura

def area(self):
    return self.largura * self.altura

def perimetro(self):
    return 2 * (self.largura + self.altura)

def imprimir_informacoes(forma):
print("Área:", forma.area)
print("Perímetro:", forma.perimetro)

circulo1 = Circulo(5)
retangulo1 = Retangulo(4, 6)

imprimir_informacoes(circulo1)
imprimir_informacoes(retangulo1)

circulo2 = Circulo("10")
retangulo2 = Retangulo(3, "8")

imprimir_informacoes(circulo2)
imprimir_informacoes(retangulo2)