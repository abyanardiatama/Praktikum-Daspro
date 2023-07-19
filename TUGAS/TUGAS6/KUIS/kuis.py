def Tail(L):
    return L[1:]
def is_empty(L):
    return L==[]
def NbElmt(L):
    
    if is_empty(L):
        return 0
    else:
        print(L)
        return 1 + NbElmt(Tail(L))
L=[1,2,3,4,5]
print(NbElmt(L))
