import random

__author__ = 'ngraydon'

# random.randrange(1, 7) - Pick a random number between 1 and 7
# Bag contains O I S Z L J T

# Static Bag will never be modified within the program
#  it will be copied onto volatileBag which can then be modified freely
staticBag = ['O', 'I', 'S', 'Z', 'L', 'J', 'T']
volatileBag = staticBag[:]

# Check that all pieces were copied into the bag
# print('Length of volatileBag = ', len(volatileBag)) 

counter = 50                        # Problem requires that you output a string of 50 pieces

while counter != 0:
                                    # if the size of the bag is 1, then clear the bag, decrease the counter, and copy back in the pieces from the original bag
    if len(volatileBag) == 1:
        print(volatileBag[0],end="")# Print out the final value of the array
        print()
        counter -= 1
        del volatileBag             # Delete the volatileBag variable out of memory
        volatileBag = staticBag[:]  # Re-create the volatileBag, as a copy of staticBag
    else:
        # print('BagSize = ', len(volatileBag))         # Print out the current size of the bag
        piece = random.randrange(0, len(volatileBag))   # Pick a random piece from within the CURRENT bag, regardless of the bags size
        # print('Piece = ', piece)  # Debug statement to specify the exact piece picked.
        print(volatileBag[piece],end="") # Print out the currently selected piece
        del(volatileBag[piece])     # Delete the current piece from the volatile bag so you cannot get the same piece within the same 'bag'
        counter -= 1
