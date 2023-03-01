class City:
    def __init__(self, name, population):
        self.__name = name
        self.__population = population

    def get_name(self):
        return self.__name
    
    def get_population(self):
        return self.__population

    def add_population(self):
        self.__population += 1

class Person:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city

    def add_population(self):
        self.__city.add_population()

    
paris = City("Paris", 1000000)
marseille = City("Marseille", 861635)


print(f"Population of {paris.get_name()}: {paris.get_population()}")
print(f"Population of {marseille.get_name()}: {marseille.get_population()}")

john = Person("John", 45, paris)
myrtille = Person("Myrtille", 4, paris)
chloe = Person("Chloé", 18, marseille)

john.add_population()
myrtille.add_population()
chloe.add_population()

print(f"Population of {paris.get_name()}: {paris.get_population()}")
print(f"Population of {marseille.get_name()}: {marseille.get_population()}")
