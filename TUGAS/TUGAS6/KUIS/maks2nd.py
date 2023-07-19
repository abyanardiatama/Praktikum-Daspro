def isEmpty(L):
    return L==[]
def First(L):
    return L[0]
def Tail(L):
    return L[1:]
def maks(L):
    if(isEmpty(L)):
        return m
    else:
        if(First(L)>m):
            m=First(L)
            return maks(Tail(L),m)
        else:
            return maks(Tail(L),m)
def maks2(L,m2):
    if(maks(L,m)-First(L)<maks(L,m)-First(Tail(L))):
        m2=First(Tail(L))
        return maks2(Tail(L),m2)
    elif(maks(L,m)-First(L)==maks(L,m)-First(Tail(L))):
        m2=First(Tail(L))
        return maks2(Tail(L),m2)
    else:
        return maks2(Tail(L),m2)
L=[12,43,43,56]
print(maks(L))
print(maks2(L,0))

