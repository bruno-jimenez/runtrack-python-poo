class Animal:
    def __init__(self, age, nom):
        self.age = age
        self.nom = nom

    def vieillir(self):
        print("L'age de l'animal est ", self.age, "ans")
        self.age += 1
        print("L'age de l'animal est ", self.age, "ans")

    def nommer(self):
        self.name = "tyber"
        print("L'animal s'appelle ", self.name)


animal = Animal(0, "")
animal.vieillir()
animal.nommer()
