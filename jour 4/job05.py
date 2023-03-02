class Forme:

    def __init__(self):
        pass

    def aire(self):
        return 0

class Rectangle(Forme):

    def __init__(self, longueur, largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

class Cercle(Forme):
        def __init__(self, rayon):
            super().__init__()
            self.rayon = rayon

        def aire(self):
            return 3.14 * self.rayon ** 2



rect = Rectangle(1, 3)
print(f"aire du rectangle {rect.aire()}")

cercle = Cercle(6)
print(f"aire du cercle {cercle.aire()}")