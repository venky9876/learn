# Write a program that performs base conversion. The input is a string, an integer b1, and anoother integer b2. The string represents an integer in base b1. The output should be the string representing the integer in base b2. Assume 2 <= b1, b2 <= 16.

# Hint : What base can you easily convert to and from ?

import string

def convert_base(num_str, b1, b2):

    is_neg = (num_str[0] == "-")
    intt = 0

    for i in range(is_neg, len(num_str)):
        intt = b1*intt + string.hexdigits.index(num_str[i].lower())
    
    final_str = []
    while True:
        final_str.append(string.hexdigits[intt%b2].upper())
        intt = intt//b2
        if intt == 0:
            break
    
    return ('-' if is_neg else '') + (''.join(reversed(intt)))



    

