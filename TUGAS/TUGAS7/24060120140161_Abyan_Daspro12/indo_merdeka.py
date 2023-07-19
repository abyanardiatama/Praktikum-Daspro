def maks(a,b):
    if a<b:
        return b
    else:
        return a
def maksL(L,maksimum):
    if(L==[]):
        return maksimum
    else:
        return maksL(L[1:],maks(L[0],maksimum))
#L=[[1,5,6,2,2],4]
#print(maksL(L[0],0))
def harga_pasukan(L,p,n):
    if(L==[]):
        return (p+n)*1000000
    else:
        if(type(L[0])==list):
            return harga_pasukan(L[1:],  p, n+maksL(L[0],0))
        else:
            return harga_pasukan(L[1:],maks(L[0],p),n)
import ast
L= ast.literal_eval(input())
print(harga_pasukan(L,0,0))
