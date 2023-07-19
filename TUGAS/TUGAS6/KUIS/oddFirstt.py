def isEmpty(L):
    return L==[]
def konso(x,L):
    return [x]+L
def First(L):
    return L[0]
def Tail(L):
    return L[1:]
def genap(L,L1):
    if(isEmpty(L)):
        return []
    else:
        if(First(L)%2==0):
            return konso(First(L),genap(Tail(L),L1))
        else:
            return genap(Tail(L),L1)
def ganjil(L,L1):
    if(isEmpty(L)):
        return []
    else:
        if(First(L)%2!=0):
            return konso(First(L),ganjil(Tail(L),L1))
        else:
            return ganjil(Tail(L),L1)
def oddFirst(L):
    return ganjil(L,L1) + genap(L,L1)
L=[int(x) for x in input().split()]
L1=[]
print(ganjil(L,L1))
print(genap(L,L1))
print(oddFirst(L))
        
