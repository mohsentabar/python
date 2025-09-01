class Fly() :
    def __init__(self , x):
        self.capacity = x
        self.passengers = []


fly1 = Fly(3) 

print(fly1.capacity)