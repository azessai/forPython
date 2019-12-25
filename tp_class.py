class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart
def afficherComplex(z):
    if z.i > 0:
        signe = '+'
    else:
        signe = '-'
    print('z = ', z.r, signe, 'i * ',abs(z.i))


z = Complex(3.0, -4.5)
afficherComplex(z)
