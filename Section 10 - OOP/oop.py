class Kettle(object):

    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwwood = Kettle('Kenwood', 8.99)
print(kenwwood.make)
print(kenwwood.price)

kenwwood.price = 12.75
print(kenwwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwwood.make, kenwwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwwood)
print(kenwwood.on)


print('*' * 80)
kenwwood.power = 1.5
print(kenwwood.power)
# print(hamilton.power)

print(Kettle.power_source)
print(kenwwood.power_source)
print(hamilton.power_source)

print("Switch to atomic power")
Kettle.power_source = 'atomic'
print(Kettle.__dict__)
print(kenwwood.__dict__)
print(hamilton.__dict__)
