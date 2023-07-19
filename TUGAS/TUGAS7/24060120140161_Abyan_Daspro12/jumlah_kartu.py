import ast
def jumlah_kartu(L):
    if(L==[]):
        return 0
    else:
        if(type(L[0])==list):
            return jumlah_kartu(L[0]) + jumlah_kartu(L[1:])
        else:
            return 1 + jumlah_kartu(L[1:])
L= ast.literal_eval(input())
print(jumlah_kartu(L))
                        
                                    
