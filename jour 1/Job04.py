class Personne():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

#[-------------------------------------]
#   creating the presentation function 
#[-------------------------------------]

    def SePresenter(self):
        print("Je suis ", self.nom, self.prenom)


personne1 = Personne("Jimenez", "Bruno")
personne1.SePresenter()
personne2 = Personne("je s'appele", "Groot")
personne2.SePresenter()
