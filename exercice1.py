def test_distinct(tab):
    i = 0
    while i < len(tab):
        j = i + 1
        while j < len(tab):
            if tab[i] == tab[j]:
                return False
            j = j + 1
        i = i + 1
    return True

print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))