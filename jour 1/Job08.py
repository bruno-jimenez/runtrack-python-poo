class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self):
        self.rayon = 5

    def circonference(self):
        circonference = self.rayon * self.rayon * 3.14
        return circonference

    def aire(self):
        aire = self.rayon * self.rayon * 3.14
        return aire

    def diametre(self):
        diametre = self.rayon * 2
        return diametre

#[--------------------------------------------------]
#  function for return all information of the circle
#[--------------------------------------------------] 

    def afficherInfos(self):
        print("La circonference est de", self.circonference())
        print("L'aire est de", self.aire())
        print("Le diametre est de", self.diametre())

cercle1 = Cercle(4)
cercle1.circonference()
cercle1.aire()
cercle1.diametre()
cercle1.afficherInfos()

cercle2 = Cercle(7)
cercle2.circonference()
cercle2.aire()
cercle2.diametre()
cercle2.afficherInfos()