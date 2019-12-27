class Eleve:
    def __init__(self, nom, age, taille=150):
        self.nom = nom
        self.age = age
        self.taille = taille
        print("Nouveau joueur : ", self.nom, 'agé de', self.age, 'ans et mesure', self.taille, 'cm')

eleve1 = Eleve("Mohammed", 17, 170)
eleve2 = Eleve("Said", 16, 160)
eleve3 = Eleve("Djelloul", 15)