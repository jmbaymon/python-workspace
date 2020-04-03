
class Diner:

    def __init__(self, name, cuisine_type, number_served =0):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_diner(self):
        print('Name: ' , self.name)
        print('Type of Diner: ' , self.cuisine_type)

    def open_diner(self):
        print("OPEN")
    def set_number_served(self, num):
        self.number_served = num
        print("new set number: ", self.number_served)
    def increment_number_served(self,numInc):
        self.number_served += numInc
        print("Number: ",self.number_served)


arby = Diner("Arby", "Fast Food")
S = Diner("Arby", "Fast Food")
arby = Diner("Arby", "Fast Food")
print(arby.name)
print(arby.cuisine_type)
print(arby.number_served)

arby.describe_diner()
arby.open_diner()
arby.set_number_served(4)
arby.increment_number_served(8)



