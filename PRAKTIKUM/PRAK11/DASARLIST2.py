
def is_empty(L):
    return L==[]
def FirstL(L):
    if is_empty(L):
        return []
    else:
        return L[0]
def LastL(L):
    return L[-1]
def Konslo(L,S):
    return L+S
def NbElmt(L):
    if is_empty(L):
        return 0
    else:
        return 1 + NbElmt(TailL(L))
def Konsl(S,L):
    return S+L
def TailL(L):
    return L[1:]
def HeadL(L):
    return L[:-1]
def is_atom(S):
    if type(S)==list and NbElmt(S)==1:
        return True
    else:
        return False
def is_list(S):
    if type(S)==int:
        return False
    else:
        return not is_atom(S)
def LastL(L):
    return L[-1]
def is_equal(L1,L2):
    if is_empty(L1) and is_empty(L2):
        return "True"
    elif is_empty(L1) and not is_empty(L2):
        return "False"
    elif not is_empty(L1) and is_empty(L2):
        return False
def IsEqS(S1,S2):
    if is_empty(S1) and is_empty(S2):
        return True
    elif not is_empty(S1)and is_empty(S2):
        return False
    elif is_empty(S1) and not is_empty(S2):
        return False
    elif not is_empty(S1) and is_empty(S2):
        if is_atom(FirstL(S1)) and is_atom(FirstL(S2)):
            return FirstL(S1) == FirstL(S2) and IsEqS(TailL(S1),TailL(S2))
        elif IsList(FirstL(S1)) and IsList(FirstL(S2)):
            return IsEqS(First(S1),First(S2)) and IsEqS(Tail(S1),Tail(S2))
        else:
            return False
def is_memberS(A,S):
    if S==[]:
        return False
    else:
        if is_atom(FirstL(S)) and FirstL(S)==A:
            return True
        else:
            return is_memberS(A,Tail(S))
def is_memberLS(L,S):
    if is_empty(S):
        if is_empty(L):
            return True
        else:
            return False
    elif not is_empty(S) and is_empty(L):
        return False
    elif not is_empty(S) and not is_empty(L):
        if is_atom(FirstL(S)):
            return is_memberLS(TailL(L),S)
        else:
            if IsEqual(L,FirstL(S)):
                return True
            else:
                is_member(L,TailL(S))

def RemberS(A,S):
    if is_empty(S):
        return S
    else:
        if is_list(FirstL(S)):
            return Konslo(RemberS(A,FirstL(S)),RemberS(A,TailL(S)))
        else:
            if FirstL(S) == A:
                return RemberS(A,TailL(S))
            else:
                Konslo(FirstL(S),RemberS(A,TailL(S)))
def rembers(a,s):
    if is_empty(s):
        return []
    else:
        if is_list(s):
            if is_memberLS(a,FirstL(FirstL(s))):
                return rembers(a,FirstL(FirstL(s))) + TailL(s)
def max2(a,b):
    if a>b:
        return a
    else:
        return b
def isOne(L):
    return NbElmt(L)==1
def maks(S):
    if isOne(S):
        if is_atom(FirstL(S)):
            return FirstL(S)
        else:
            return maks(FirstL(S))
    else:
        if is_atom(FirstL(S)):
            return Max2(First(S),maks(Tail(S)))
        else:
            return Max2(maks(First(S)),maks(Tail(S)))
  
S=[1,2,3,[2,3,4]]
S2=[[3,6,4],6,32,[6,4]]
S3=[6]
S4=[5,3,[5,3,3],7,5]

def faktor(n,count):
    if(n == count):
        return 1
    elif(n % count == 0):
        return 1 + faktor(n,count+1)
    else:
        return faktor(n,count+1)
        
def IsPrime(n):
    if(faktor(n,1) == 2):
        return True
    else:
        return False
    
def LPrime(L):
    if is_empty(L):
        return []
    else:
        if IsPrime(First(L)):
            return konso(First(L),LPrime(Tail(L)))
        else:
            return Rember(First(L),LPrime(Tail(L)))

def IsListPrime(L):
    if is_list(L):
        if IsPrime(FirstL(L)):
            return True
        else:
            return False
    elif IsPrime(FirstElmt(L)):
        return IsListPrime(Tail(L))
    else:
        return False
