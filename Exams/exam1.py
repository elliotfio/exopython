def plus_long_palindrome(s):
    meilleur = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sous = s[i:j]
            if sous == sous[::-1] and len(sous) > len(meilleur):
                meilleur = sous
    return meilleur


print(plus_long_palindrome("babad"))
print(plus_long_palindrome("cbbd"))


