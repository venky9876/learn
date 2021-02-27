# Implement a method to perform basic string compression using the counts of repeated characters. For exmple, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method shold return original  string. You can assume the string has only uppercase and lowercase letter (a-z)

def string_compression(strr):
    #strr = list(strr)
    j = 0
    final = []

    for i in range(len(strr)):
        if strr[i-1] != strr[i]:
            final += [strr[i-1], str(j)]
            j = 0
        j += 1
    final += [strr[-1], str(j)]
    print (final)
    return min(strr,''.join(final), key=len)


if __name__ == "__main__":

    strr = "aabcccccaaa"

    print (string_compression(strr))




