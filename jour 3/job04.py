class Joueur:
    def __init__(self, nom, numero, position, buts, passes, jaunes, rouges):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.jaunes = jaunes
        self.rouges = rouges

    def marquerUnBut(self):
        self.buts += 1


    def effectuerUnePasseDecisive(self):
        self.passes += 1


    def recevoirUnCartonJaune(self):
        self.jaunes += 1


    def recevoirUnCartonRouge(self):
        self.rouges += 1


    def afficherStatistiques(self):
        print("\nNom : ", self.nom)
        print("Numero : ", self.numero)
        print("Position : ", self.position)
        print("Buts : ", self.buts)
        print("Passes : ", self.passes)
        print("Cartons jaunes : ", self.jaunes)
        print("Cartons rouges : ", self.rouges)


class Equipe:

    def __init__(self, nom, joueurs=[]):
        self.nom = nom
        self.joueurs = joueurs


    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)


    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStatistiques()


    def mettreAJourStatistiquesJoueur(self, joueur):
        joueur.afficherStatistiques()


# Test #
joueur1 = Joueur("Sanchez", 70, "Attaquant", 0, 0, 0, 0)
joueur2 = Joueur("Under", 17, "Attaquant", 0, 0, 0, 0)
joueur3 = Joueur("Payet", 10, "Attaquant", 0, 0, 0, 0)
joueur4 = Joueur("Guendouzi", 6, "Attaquant", 0, 0, 0, 0)
joueur5 = Joueur("CLauss", 23, "Defenseur", 0, 0, 0, 0)
joueur6 = Joueur("Gigot", 4, "Defenseur", 0, 0, 0, 0)
joueur7 = Joueur("Bailly", 3, "Defenseur", 0, 0, 0, 0)
joueur8 = Joueur("Lopez", 16, "Gardien", 0, 0, 0, 0)

equipe1 = Equipe("Olympyque de Marseille")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
equipe1.ajouterJoueur(joueur4)
equipe1.ajouterJoueur(joueur5)
equipe1.ajouterJoueur(joueur6)
equipe1.ajouterJoueur(joueur7)
equipe1.ajouterJoueur(joueur8)

equipe1.afficherStatistiquesJoueurs()

joueur1.marquerUnBut()
joueur1.effectuerUnePasseDecisive()
joueur1.recevoirUnCartonJaune()

joueur1.afficherStatistiques()
