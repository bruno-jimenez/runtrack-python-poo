class Livre:
    def __init__(self):
        self.__titre = "Republic commando : True color"
        self.__auteur = "Karen Travis"
        self.__nbpages = 482

    def __gettitre(self):
        return self.__titre

    def __getauteur(self):
        return self.__auteur

    def __getnbpages(self):
        return self.__nbpages

    def modifyvalues(self):
        self.__gettitre()
        self.__getauteur()
        self.__getnbpages()

        self.__titre = "La croisade noir du jedi fou"
        self.__auteur = "Timothy Zahn"
        self.__nbpages = 986

#[-----------------------------]
#  verification of page number
#[-----------------------------] 

        if self.__nbpages % 2 != 0:
            print("Nombre de pages incorrect")
        else:
            print("the title is", self.__titre, ", the author are", self.__auteur, "the book contain", self.__nbpages ,"page .")


livre = Livre()
livre.modifyvalues()
