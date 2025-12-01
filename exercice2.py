print("Premier nombre:")
a = int(input())
print("Second nombre :")
b = int(input())
print("Troisième nombre :")
c = int(input())

if (a >= b and a <= c) or (a <= b and a >= c):
    mediane = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    mediane = b
else:
    mediane = c

print("Médiane des trois nombres:")
print(mediane)


