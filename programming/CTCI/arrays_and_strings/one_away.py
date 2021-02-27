# There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit(or zero edits) away

def one_edit_replace(str1, str2):

    edited = False
    for ele1, ele2 in zip(str1, str2):
        if ele1 != ele2:
            if edited == True:
                return False
            else:
                edited = True
    return True

def one_edit_insert(str1, str2):

    edited = 0
    i = j= 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if edited == True:
                return False
            else:
                edited = True
                j += 1
        else:
            i += 1
            j += 1
    return True



def one_away(str1, str2):

    if len(str1) == len(str2):
        return one_edit_replace(str1, str2)

    if len(str1) - 1 = len(str2):
        return one_edit_insert(str1, str2)

    if len(str1) + 1 = len(str2):
        return one_edit_insert(str2, str1)

    return False

