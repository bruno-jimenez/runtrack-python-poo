class Rectangle:
    def __init__(self):
        self.longueur = 10
        self.largeur = 5

    def __getlongueur(self):
        self.__init__()
        return self.longueur

    def __getlargeur(self):
        self.__init__()
        return self.largeur

    def showvalues(self):
        self.__getlongueur()
        self.__getlargeur()

        self.largeur = 15
        self.longueur = 20
        print("Longueur =", self.longueur, "Largueur =", self.largeur)


rectangle = Rectangle()
rectangle.showvalues()

