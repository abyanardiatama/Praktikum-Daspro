def addSaham(x,y,L):
    return [[x,y]]
def first(L):
    return L[0]
def tail(L):
    return L[1:]
def bantuRias(x):
    hasil=0
    if(x==0):
        return 0
    L.append(list(map(int,input().split())))
    hasil += L[-1][1] - L[-1][0]
    return hasil*100 + bantuRias(x-1)
x=int(input())
L=[]
print(bantuRias(x))
