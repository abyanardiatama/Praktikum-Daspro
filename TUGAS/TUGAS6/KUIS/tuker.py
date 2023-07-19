def first(L):
    return L[0]
def tail(L):
    return L[1:]
def is_empty(L):
    return L==[]
def permenManis(L1,L2):
    temp=0
    count=0
    if(L1==[] or L2==[]):
        return 0
    else:
        if(first(L1)<first(L2)):
            temp=L1[0]
            L1[0]=L2[0]
            L2[0]=temp
            return 1 + permenManis(tail(L1),tail(L2))
        else:
            return permenManis(tail(L1),tail(L2))

n=int(input())
L=list(map(int,input().strip().split()))[:n]
L1=list(map(int,input().strip().split()))[:n]
print(permenManis(L,L1))
