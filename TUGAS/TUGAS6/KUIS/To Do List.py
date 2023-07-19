def konsi(P,x):
    return P + [x]
def Tail(P):
    return P[1:]
def NbElmt(P):
    if(P==[]):
        return 0
    else:
        return 1 + NbElmt(Tail(P))

def todolist(P,n):
    if(n<=0):
        return P
    else:
        return todolist(konsi(P,x=input()),n-1)
P=[]
n=int(input())
if(n<=0):
    print("Tobi tidak ingin bermalas-malasan")
elif(n>9):
    print("Tobi tidak bisa bekerja terlalu keras!")
print(todolist(P,n))

