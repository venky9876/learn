
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1

    return num_bits

if __name__ == "__main__":

    y = 4333
    num_bits = count_bits(y)
    print ("bits of : %s is %s" %(y,num_bits))
