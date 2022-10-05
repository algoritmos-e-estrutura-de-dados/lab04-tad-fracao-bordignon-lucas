import math

class Fracao:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def add(self, fracao):
        num = (self.numerador * fracao.denominador) \
        + (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def sub(self, fracao):
        num = (self.numerador * fracao.denominador) \
        - (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def mult(self, fracao):
        num = self.numerador * fracao.numerador
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def division(self, fracao):
        num = self.numerador * fracao.denominador
        den = self.denominador * fracao.numerador
        return Fracao(num, den)

    def simplification(self):
        commom_divisor = math.gcd(self.numerador, self.denominador)
        num = self.numerador / commom_divisor
        den = self.denominador / commom_divisor
        return Fracao(num, den)

        
    def show(self):
        print(self.numerador,'/',self.denominador)
        

print('Fração 1')
fracao1 = Fracao(100,50)
fracao1.show()

print('Fração 2')
fracao2 = Fracao(50,50)
fracao2.show()
