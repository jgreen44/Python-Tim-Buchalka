class Kettle(object):
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False


kenwwood = Kettle('Kenwood', 8.99)
print(kenwwood.make)
print(kenwwood.price)

kenwwood.price = 12.75
print(kenwwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwwood.make, kenwwood.price, hamilton.make, hamilton.price))
