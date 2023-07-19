def isEmpty(L):
    return L==[]
def First(L):
    return L[0]
def Tail(L):
    return L[1:]
def Akatsuki(L,m,i):
    if(isEmpty(L)):
        return i
    else:
        if(First(L)>=m):
            i=i+1
            return Akatsuki(Tail(L),m,i)
        else:
            return Akatsuki(Tail(L),m,i)
    
m=int(input())
L=[int(x) for x in input().split()]
print(Akatsuki(L,m,0))
