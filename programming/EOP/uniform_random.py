# How would you implement a uniform ranom number generator that generates a random number i between a and b, inclusive, given a random number generator that produces 0 or 1 with equal probability 




import math
import numpy as np

### NOT COMPLETE

def uniform_random(lower_bound, upper_bound):
    rand_num = ''

    rand_range = upper_bound - lower_bound + 1

    while True:

        for i in range(rand_range):
            #print (i)
            rand_num += str(np.random.randint(2))
        
        print (rand_num)
        if int(rand_num,2) < rand_range:
            break
    
    return lower_bound + rand_range


if __name__ == "__main__":

    lower_bound = 10
    upper_bound = 20

    rand_num = uniform_random(lower_bound, upper_bound)

    print("Rand number between %s and %s is %s"%(lower_bound, upper_bound, rand_num))


