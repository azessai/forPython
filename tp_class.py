class Complex:
    def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

    def afficherComplex(self):
        if self.i > 0:
            signe = '+'
        else:
            signe = '-'
        print('z = ', self.r, signe, 'i * ',abs(self.i))


z = Complex(3.0, -4.5)
z.afficherComplex()
z = Complex(2.0, 4)
z.afficherComplex()