# Write a program that takes as input a permutation, and returns the next permutation under dictionary ordering. If the permutation is the last permutation, return the empty array. For example, if the input is [1,0,3,2] your function should return [1,2,0,3]. If the input is [3,2,1,0], return [].

def next_permutation(arr):

    return arr

if __name__ == "__main__":

    arr = [1,2,0,4]

    next_arr = next_permutation(arr)

    print ("Next permutation is %s"%next_arr)

    