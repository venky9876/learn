
# Find if a given integer is palindrome

### Not complete

import math

def palindrome_bf(x):

    x_len = len(str(x))
    temp_x = x

    for i in range(1,math.floor(x_len/2)):
        if (int(temp_x/pow(10,(x_len-i))) != (temp_x%pow(10,i))):
            return False
        temp_x = temp_x//pow(10,i)
        temp_x = temp_x%pow(10,(x_len-i))
        
        print (i,temp_x)
    return True




def palindrome(x):
    
    return

if __name__ == "__main__":

    x = 543345
    #print ("hello")
    flag = palindrome_bf(x)
    print ("Is %s palndrome : %s"%(x,flag))
