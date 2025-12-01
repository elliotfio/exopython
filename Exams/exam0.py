texte = input("Saisir une phrase ")

mots = texte.split()

if len(mots) == 0:
    print(0)
else:
    dernier = mots[len(mots) - 1]
    print(len(dernier))


