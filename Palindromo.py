def palindromo(string):
    i = 0 
    j = len(string)-1
    while j >= 0:
        if string[i] != string[j]:
            return False
        i = i + 1
        j = j - 1
    return True

print(palindromo('aba'))
