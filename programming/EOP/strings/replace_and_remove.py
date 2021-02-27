# Write a program which takes as input an array of characters, and removes each 'b' and replaces each 'a' by two 'd's. Specifically, along with the array, you are provided an integer-valued size. Size denotes the number of entries of the array that the operation is to be applied to. You do not have to worry about preseving subsequent entries. For example, if the array [a,b,a,c,d] and the size is 4, then you can return [d,d,d,d,c]. You can assume there is enough space in the array to hold the final result.

### Hint : Consider performing multiples passes on S.

def replace_and_remove(strr, count):

    if len(strr) == 0 or count == 0:
        return strr
    else:
        if strr[0] == 'a':
            return ['d','d'] + replace_and_remove(strr[1:], count - 1)
        elif strr[0] == 'b':
            return replace_and_remove(strr[1:], count - 1)
        else:
            return [strr[0]] + replace_and_remove(strr[1:], count -1)

if __name__ == "__main__":

    strr = ['a','b','a','a', 'c','d']
    count = 3

    final = replace_and_remove(strr, count)

    print ("final list %s"%final)



