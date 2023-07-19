def jumlah_ganjil(L):
    if(L==[]):
        return 0
    else:
        if(type(L[0])==list):
            return jumlah_ganjil(L[0]) + jumlah_ganjil(L[1:])
        elif(L[0]%2 != 0):
            return L[0] + jumlah_ganjil(L[1:])
        else:
            return jumlah_ganjil(L[1:])
import ast
L=ast.literal_eval(input())
print(jumlah_ganjil(L))
