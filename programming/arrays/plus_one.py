# Write a program which takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D+1.

import copy

def plus_one(array_int):


    for i in reversed(range(len(array_int))):
        array_int[i] += 1
        if array_int[i] == 10:
            array_int[i] = 0
        else:
            break

    if array_int[0] == 0:
        array_int[0] = 1
        array_int.append(0)
    return array_int

if __name__ == "__main__":

    array_int = [9,9]
    org_int = copy.deepcopy(array_int)

    op_array = plus_one(array_int)

    print ("Plus one of %s is %s"%(org_int, op_array))