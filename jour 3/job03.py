class Tache:
    
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut


    def __str__(self):
        return f"Titre: {self.titre}, Description: {self.description}, Statut: {self.statut}"
    


class ListeDeTaches:
    
    def __init__(self):
        self.taches = []


    def ajouterTache(self, tache):
        self.taches.append(tache)



    def supprimerTache(self, tache):
        self.taches.remove(tache)

    
    def marquerCommeFinie(self, tache):
        tache.statut = "Terminée"

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        for tache in self.taches:
            if tache.statut == statut:
                print(tache)

tache1 = Tache("boire", "glouglou", "A faire")
tache2 = Tache("porjet voltaire", "pls nooooo", "A faire")
tache3 = Tache("manger", "miam miam", "A faire")
tache4 = Tache("Coder", "c'est good jusqu'a demain ça", "A faire")

listeDeTaches = ListeDeTaches()
listeDeTaches.ajouterTache(tache1)
listeDeTaches.ajouterTache(tache2)
listeDeTaches.ajouterTache(tache3)
listeDeTaches.ajouterTache(tache4)

listeDeTaches.supprimerTache(tache2)
listeDeTaches.marquerCommeFinie(tache1)

listeDeTaches.afficherListe()


