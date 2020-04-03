from diner import Diner

class IceCreamStand(Diner):
    def __init__(self,name, cuisine_type, number_served =0):
        super().__init__(name, cuisine_type, number_served =0)
        self.flavors = ['Chocolate', 'Vanilla', 'Strawberry']

    def display_flavors(self):
        print(self.flavors)





chose1 = IceCreamStand('IceCircle', 'Sweets')

chose1.display_flavors()

