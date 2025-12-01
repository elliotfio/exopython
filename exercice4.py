texte = input("Saisir une chaine ")

lettres = 0
chiffres = 0

for c in texte:
    if c.isalpha():
        lettres = lettres + 1
    elif c.isdigit():
        chiffres = chiffres + 1

print("Lettres", lettres)
print("Chiffres", chiffres)


