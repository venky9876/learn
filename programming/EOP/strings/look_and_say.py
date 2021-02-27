# The look-and-say sequence starts with 1. Subsequent numbers are derived by describing the previous number in terms of consecutive digits. Specifically, to generate an entry of the sequence from the previous entry, read of the digits of the pervious entry, counting the number of digits in groups of the same digit. For example, 1; one 1; two 1s; one 2 then on 1; one 1, then one 2, then two 1s; three 1s, then two 2s, then one 1. The first eight numbers in the look-and-say sequence are [1,11,21,1211, 111221, 312211, 13112221, 1113213211]

# Write a program that takes as input an integer n and returns the nth integer in the look-and-say sequence. Return the result as a string.

import copy

def look_and_say(n):

    curr = ['1']
    i = 1
    while True:
        prev = copy.deepcopy(curr)
        curr = []
        start = 0
        end = 0
        print (prev)
        for j in range(len(prev)+1):
            print (start, end)
            if (prev[start] == prev[end]) and (end != len(prev)-1):
                end += 1
            else:
                if prev[start] != prev[end]:
                    curr += [str(end - start), prev[start]]
                    start = end
                else:
                    curr += [str(end-start+1), prev[start]]
                    break
                    

        if i == n:
            break
        else:
            i += 1
    #print (curr)

    return int(('').join(curr))

if __name__ == "__main__":

    n = 10

    num = look_and_say(n)

    print("%sth look and say number is - %s"%(n,num))



        
