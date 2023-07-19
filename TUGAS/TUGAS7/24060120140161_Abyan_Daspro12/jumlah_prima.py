def is_prima(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def jumlah_prima(L):
    if(L==[]):
        return 0
    else:
        if(type(L[0])==list):
            return jumlah_prima(L[0]) + jumlah_prima(L[1:])
        elif(is_prima(L[0])):
            return L[0] + jumlah_prima(L[1:])
        else:
            return jumlah_prima(L[1:])
import ast
L= ast.literal_eval(input())
print(jumlah_prima(L))
