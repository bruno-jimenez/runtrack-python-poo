class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

#[-------------------------------------]
#   creating the adding function 
#[-------------------------------------]

    def addition(self):
        result = self.nombre1 + self.nombre2
        print("the result are : ", result)


operation = Operation(1, 2)
operation.addition()