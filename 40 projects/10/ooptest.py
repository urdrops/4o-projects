class Car:
    def __init__(self,price,speed):
        self.price = price 
        self.speed = speed
    def show(self):
        print("the speed of car is", self.speed)
        print("the price of car is", self.price)

tesla = Car("70 000$","250km/h")
tesla.price = "unknown"
tesla.show()