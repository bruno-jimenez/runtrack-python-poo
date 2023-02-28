class Student:
    def __init__(self):
        self.__nom = "Doe"
        self.__prenom = "John"
        self.__numeroetudiant = 145
        self.__nbcredits = 0

    def get_credits(self):
        return self.__nbcredits

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def add_credits(self):
        self.get_credits()
        while self.__nbcredits < 30:
            self.__nbcredits += 10

    def show_credits(self):
        print(self.__prenom, self.__nom, "have", self.__nbcredits, "credit")

#[---------------------------]
# verification and evalution 
#[---------------------------]

    def __studentEval(self):
        if self.__nbcredits >= 90:
            Eval = "Excellent"
        elif self.__nbcredits >= 80:
            Eval = "Très Bien"
        elif self.__nbcredits >= 70:
            Eval = "Bien"
        elif self.__nbcredits >= 60:
            Eval = "Passable"
        else:
            Eval = "Insuffisant"

        return Eval

#[---------------------------]
#  print stud info 
#[---------------------------]

    def studentInfo(self):
        print("Nom =", self.__nom)
        print("Prenom =", self.__prenom)
        print("ID =", self.__numeroetudiant)
        print("Niveau =", self.__studentEval())


student = Student()
student.get_credits()
student.get_nom()
student.get_prenom()
student.add_credits()
student.show_credits()
student.studentInfo()
