def palindrom(x):
    if x == x[::-1]:
        return "YA"
    else:
        return "BUKAN"

kata = str(input())
print(palindrom(kata))
