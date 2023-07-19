#Konso nambah elemen di depan
#Kons nambah elemen di belakang
def konso(L,x):
    return [x]+L

def kons(L,x):
    return L + [x]

def Firstelmt(L):
    return

def LastElmt(L):
    return

def Tail(L):
    if (not(L==[])):
        return L[1:]

def Head(L):
    if(not(L==[])):
        return L[:-1]

def is_empty(L):
    return L==[]

def Nbelement(L):
    if L==[]:
        return 0
    else:
        return Nbelement(Tail(L))+1

def copy(L):
    if is_empty(L):
        return L
    else:
        Konso(Firstelmt(L),copy(Tail(L)))

def is_OneElmt(L):
    if (nElmt==1):
        return "True"
    else:
        return "False"

def is_equal(L1,L2):
    if is_empty(L1) and is_empty(L2):
        return "True"
    elif is_empty(L1) and not is_empty(L2):
        return "False"
    elif not is_empty(L1) and is_empty(L2):
        return False

def is_member(L,e):
    if (L==[]):
        return "False"
    else:
        return is_member(Tail(L),e)

def invers(L):
    if l==[]:
        return[]
    else:
        return Konso(Lastelmt(L),Invers(Head(L)))
