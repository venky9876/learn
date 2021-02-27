# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dicitionary words.

def is_permut_palin(strr):

    str_dict = {}

    countodd = 0

    for ele in strr:
        if ele not in str_dict.keys():
            str_dict[ele] = 1
            countodd += 1
        else:
            str_dict[ele] += 1
            if str_dict[ele] % 2 == 0:
                countodd -= 1
            else:
                countodd += 1


    
    return (countodd <= 1)

    


