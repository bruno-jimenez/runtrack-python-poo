class Voiture:
    def __init__(self):
        self.__marque = "Dodge"
        self.__modele = "RAM TRX"
        self.__annee = 2023
        self.__kilometrage = 25000
        self.__en_marche = False
        self.__reservoir = 125

    def get_marque(self):
        return self.__marque

    def change_marque(self):
        self.get_marque()

    def get_modele(self):
        return self.__modele

    def change_model(self):
        self.get_modele()

    def get_annee(self):
        return self.__annee

    def change_annee(self):
        self.get_modele()

    def get_kilometrage(self):
        return self.__kilometrage

    def change_kilometrage(self):
        self.get_kilometrage()

    def get_en_marche(self):
        return self.__en_marche

    def change_en_marche(self):
        self.get_en_marche()

    def get_reservoir(self):
        return self.__reservoir

    def change_reservoir(self):
        self.get_reservoir()

    def verifier_plein(self):
        return self.__reservoir

    def demarrer(self):
        if self.verifier_plein() > 5:
            self.__en_marche = True

    def arreter(self):
        self.__en_marche = False
