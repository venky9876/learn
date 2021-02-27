# Implement a function for reversing the words in a string s.

def reverse_words(strr):

    strr = list(strr)

    if not strr:
        return None

    for i in range(len(strr)//2):
        strr[i], strr[~i] = strr[~i], strr[i]


    start = 0
    end = 0

    while True:

        if (strr[end] != ' ') and (end != len(strr)-1):
            #print (strr[end])
            end += 1
        else:
            #print (end)
            for i in range(start, start + (end - start-1)//2):
                strr[i], strr[end - i + start-1] = strr[end-i+start-1], strr[i]

            if end == len(strr) - 1:
                break
            end += 1
            start = end

    return ('').join(strr)

if __name__ == "__main__":

    strr = "Bob likes Alice"   

    strr = reverse_words(strr)

    print (strr)     



