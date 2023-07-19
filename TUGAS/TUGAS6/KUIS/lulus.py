def nol(q):
    return q[0]
def tail(q):
    return q[1:]
def lulus(batas,nilai):
    if(nilai==[]):
        return 0
    elif(nol(nilai)>batas):
        return 1 + lulus(batas,tail(nilai))
    else:
        return lulus(batas,tail(nilai))
n=int(input())
L=[int(x) for x in input().split()]
print(lulus(n,L))
