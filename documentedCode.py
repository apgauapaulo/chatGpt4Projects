import math

"""
Este código em Python define duas classes, uma para representar um círculo e outra para representar um retângulo, bem como uma função para imprimir informações de uma forma geométrica.
A classe Circulo possui um construtor que recebe o valor do raio como parâmetro e armazena esse valor em um atributo da classe. Além disso, há dois métodos: area() e perimetro(), que calculam e retornam a área e o perímetro do círculo, respectivamente, utilizando fórmulas matemáticas definidas na biblioteca math do Python.
A classe Retangulo também possui um construtor que recebe os valores da largura e altura como parâmetros e armazena esses valores em atributos da classe. Ela também possui dois métodos: area() e perimetro(), que calculam e retornam a área e o perímetro do retângulo, respectivamente, utilizando fórmulas matemáticas.
A função imprimir_informacoes(forma) recebe como parâmetro um objeto da classe Circulo ou da classe Retangulo, e imprime na tela a área e o perímetro dessa forma geométrica, utilizando os métodos area() e perimetro() da classe correspondente.
No final do código, são criados um objeto da classe Circulo com raio 5 e um objeto da classe Retangulo com largura 4 e altura 6. Em seguida, as informações de cada objeto são impressas na tela utilizando a função imprimir_informacoes(). O resultado da execução do código será a impressão da área e do perímetro do círculo e do retângulo criados.
"""

# Classe para representar um círculo
class Circulo:
    # Inicializa o objeto com o valor do raio
    def __init__(self, raio):
        self.raio = raio

    # Calcula e retorna a área do círculo
    def area(self):
        return math.pi * self.raio ** 2

    # Calcula e retorna o perímetro do círculo
    def perimetro(self):
        return 2 * math.pi * self.raio

# Classe para representar um retângulo
class Retangulo:
    # Inicializa o objeto com os valores da largura e altura
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    # Calcula e retorna a área do retângulo
    def area(self):
        return self.largura * self.altura

    # Calcula e retorna o perímetro do retângulo
    def perimetro(self):
        return 2 * (self.largura + self.altura)

# Função para imprimir informações (área e perímetro) de uma forma geométrica
def imprimir_informacoes(forma):
    print("Área:", forma.area())
    print("Perímetro:", forma.perimetro())

# Instanciando um círculo com raio 5 e um retângulo com largura 4 e altura 6
circulo1 = Circulo(5)
retangulo1 = Retangulo(4, 6)

# Imprimindo informações do círculo e retângulo criados
imprimir_informacoes(circulo1)
imprimir_informacoes(retangulo1)
