
def parity(x):
    result  = 0
    while x:
        result ^= x & 1
        x >>=1
    return result

if __name__ == "__main__":

    var = 1
    par_var = parity(var)
    print ("parity of %s is %s"%(var, par_var))

