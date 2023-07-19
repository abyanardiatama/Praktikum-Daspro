#Konso nambah elemen di depan
#Kons nambah elemen di belakang
def Konso(x,L):
    return [x]+L
def Kons(L,x):
    return L + [x]
###################################################################
def First(L):
    return L[0]
def Last(L):
    return L[-1]
###################################################################
def Tail(L):
    if (not(L==[])):
        return L[1:]
def Head(L):
    if(not(L==[])):
        return L[:-1]
###################################################################
def IsEmpty(L):
    return L==[]
###################################################################
def NbElmt(L):
    if L==[]:
        return 0
    else:
        return NbElmt(Tail(L))+1
###################################################################
def Copy(L):
    if IsEmpty(L):
        return L
    else:
        Konso(First(L),Copy(Tail(L)))
###################################################################
def IsOneElmt(L):
    if (NbElmt==1):
        return "True"
    else:
        return "False"
###################################################################
def IsEqual(L1,L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return "True"
    elif IsEmpty(L1) and not IsEmpty(L2):
        return "False"
    elif not IsEmpty(L1) and IsEmpty(L2):
        return False
###################################################################
def Rember(x,L):
    if IsEmpty(L):
        return []
    else:
        if First(L)==x:
            return Tail(L)
        else:
            return Konso(First(L),Rember(x,Tail(L)))
###################################################################
def IsMember(L,e):
    if IsEmpty(L):
        return False
    else:
        if First(L)== e:
            return True
        else:
            return IsMember(Tail(L),e)
###################################################################
def Invers(L):
    if L==[]:
        return[]
    else:
        return Konso(Lastelmt(L),Invers(Head(L)))
###################################################################
def IsAtom(S):
    if type(S)==list and NbElmt(S)==1:
        return True
    else:
        return False
###################################################################
def IsList(S):
    if type(S)==int:
        return False
    else:
        return not IsAtom(S)
