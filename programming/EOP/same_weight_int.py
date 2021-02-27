# Define the weight of a non-negative integer to be the number of bits that are set to 1 in its binary form. Write a program which takes input a non-negative int x and returns a number y which is not equal to x, but has the same weight as x and the difference, |x-y| is as small as possible.

def closest_int_same_bit_count(x):
    maxbits = 64
    for i in range(maxbits-1):
        if ((x>>i) & 1) != ((x>>(i+1)) & 1):
            x ^= (1 << i) | (1 << (i+1))
            return x

    raise ValueError("All bits are same")


if __name__ == "__main__":
    x = 43
    y = closest_int_same_bit_count(x)
    print ("closest int of %s with same weight is %s"%(x,y))

