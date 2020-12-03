# This program reverses an input list of integers.
# Written by: Thu Aung
# Written on: Oct 11, 2020.

# Import time module to measure how long the program takes.
import time
class Reversal:
    def __init__(self, size):
        self.size = size

    def rev_list(self):
        # Start timer
        start = time.time()
        # Create an empty list
        created_list = []
        # Create a list using input size n.
        for i in range(1, self.size +1):
            created_list.append(i)
        print(created_list)

        # Reverse the created list by swapping index[0]<-->index[-1], index[1]<-->index[-2] and so on.
        for j in range(int(len(created_list)/2)):
            k = -j-1
            created_list[j],created_list[k]= created_list[k], created_list[j]
        # Stop timer
        stop = time.time()
        print(created_list)
        print("Elapsed time: ", stop - start)