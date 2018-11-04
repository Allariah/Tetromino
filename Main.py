import random

__author__ = 'ngraydon'

# random.randrange(1, 7)
# Bag contains O I S Z L J T

staticBag = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']
volatileBag = staticBag[:]

# print('Length of volatileBag = ', len(volatileBag))


counter = 50

while counter != 0:
    if len(volatileBag) == 1:
        print(volatileBag[0],end="")
        print()
        counter -= 1
        del volatileBag
        volatileBag = staticBag[:]
    else:
        # print('BagSize = ', len(volatileBag))
        piece = random.randrange(0, len(volatileBag))
        # print('Piece = ', piece)
        print(volatileBag[piece],end="")
        del(volatileBag[piece])
        counter -= 1
