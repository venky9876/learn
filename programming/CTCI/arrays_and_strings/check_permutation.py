# Check permutation : Given two strings, write a method to decide if one is a permutation of the other
from collections import Counter

def is_permut(str1, str2):

    if len(str1) != len(str2):
        return False

    if (not str1) or (not str2):
        return False

    counter = Counter()
    for ele in str1:
        counter[ele] += 1

    for ele in str2:
        if counter[ele] == 0:
            return False
        counter[ele] -= 1

    return True

if __name__ == "__main__":

    str1 = "venky"
    str2= "enkyvv"

    print (is_permut(str1, str2))







  