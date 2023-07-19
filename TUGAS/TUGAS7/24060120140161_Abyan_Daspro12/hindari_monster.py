def hindari_monster(L,x):
    if (L==[]):
        return []
    else:
        if (type(L[0])==list):
            return [hindari_monster(L[0],x)] + hindari_monster(L[1:],x)
        elif (L[0] % x ==0):
            return hindari_monster(L[1:],x)
        else:
            return [L[0]] + hindari_monster(L[1:],x)
import ast
L=ast.literal_eval(input())
x=int(input())
print(hindari_monster(L,x))
