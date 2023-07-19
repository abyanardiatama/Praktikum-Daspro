import ast

# JUMLAH KARTU --> idea = nbelmt with a twist
# list_kartu = ast.literal_eval(input()) # list_kartu berisikan list of list

# def hitung_kartu(lol):
#     if (lol == []): # IsEmpty
#         return 0
#     else:
#         if (type(lol[0]) == list): # IsList
#             return hitung_kartu(lol[0]) + hitung_kartu(lol[1:])
#         else:
#             return 1 + hitung_kartu(lol[1:])

# print(hitung_kartu(list_kartu))

# ===========================================================================

# HINDARI MONSTER --> idea = rember
list_tag_angka = ast.literal_eval(input())
x = int(input())

def hindari_monster(lol, x):
    if (lol == []): # IsEmpty
        return []
    else:
        if (type(lol[0]) == list): # IsList
            return [hindari_monster(lol[0], x)] + hindari_monster(lol[1:], x)
        elif (lol[0] % x == 0): # IsAtom, first element kelipatan x
            return hindari_monster(lol[1:], x)
        else: # First element bukan kelipatan x
            return [lol[0]] + hindari_monster(lol[1:], x)

print(hindari_monster(list_tag_angka, x))

