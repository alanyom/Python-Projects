#Define a class called Bike that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, color and price. Assign to the variable testOne an instance of Bike whose color is blue and whose price is 89.99. Assign to the variable testTwo an instance of Bike whose color is purple and whose price is 25.0.

class Bike:
    def __init__(self, color, price):
        self.color = color
        self.price = price
    def color(self):
        return self.color
    def price(self):
        return self.price
    def __str__(self):
        return "Bike whose color is {} and whose price is {}.".format(self.color, self.price)
testOne = Bike("blue",89.99)
testTwo = Bike("purple",25.0)
