def konso(P,x):
    return [x]+P
def konsi(P,x):
    return P+[x]
def oddFirst(P,i,P2):
    if(not P2==[]):
        if(P[i]%2!=0):
            konso(P2,P[i])
            return oddFirst(P,i+1,P2)
        else:
            konsi(P2,P[i])
            return oddFirst(P,i+1,P2)
#inp = list(map(int, input().split(' ')))
P=[10,9,8,7,6,5]
P2=[]
oddFirst(P,0,P2)
