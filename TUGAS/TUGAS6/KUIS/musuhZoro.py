def first(P):
    return P[0]
def tail(P):
    return P[1:]
def maxke2(P,m1,m2):
    if(P==[]):
        return m2
    elif(first(P)>m1):
        m2=m1
        m1=first(P)
        return maxke2(tail(P),m1,m2)
    else:
        return maxke2(tail(P),m1,m2)

P=[int(x) for x in input().split()]
print(maxke2(P,0,0))
    
        
