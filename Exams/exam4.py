def incrementer(chiffres):
    retenue = 1
    i = len(chiffres) - 1
    
    while i >= 0 and retenue == 1:
        chiffres[i] = chiffres[i] + 1
        if chiffres[i] == 10:
            chiffres[i] = 0
            retenue = 1
        else:
            retenue = 0
        i = i - 1
    
    if retenue == 1:
        chiffres.insert(0, 1)
    
    return chiffres


print(incrementer([1, 2, 3]))
print(incrementer([4, 3, 2, 1]))
print(incrementer([9]))



