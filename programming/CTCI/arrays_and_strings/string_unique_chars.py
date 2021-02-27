# Is Unique : Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures ?

def is_unique(strr):
    if not strr:
        return None

    if len(strr) > 128:
        return False

    char_set = [False for _ in range(128)]

    for char in strr:

        val = ord(char)

        if char_set[val]:
            return False
        char_set[val] = True

    return True

if __name__ == "__main__":

    strr = "is venkys"

    print (is_unique(strr))

