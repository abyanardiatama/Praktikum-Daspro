def konso(x,L):
    return [x]+[L]
def Last(L):
    return L[-1]
def First(L):
    return L[0]
def Head(L):
    return L[:-1]
def Tail(L):
    return L[1:]
def is_empty(L):
    if L==[]:
        return True
def is_member(x,L):
    if is_empty(L):
        return False
    else:
        if Last(L)==x:
            return True
        elif Last(L)!=x:
            return is_member(x,Head(L))

def rember(x,L):
    if is_member(x,L):
        if is_empty(L):
            return L
        elif First(L)==x:
            return Tail(L)
        else:
            return konso(First(L),Rember(x,Tail(L)))
    else:
        return L
    

def Multirember(x,L):
    if is_member(x,L):
        
        if is_empty(L):
            return L
        
def Make_set(L):
    if is_empty(L):
        return L
    else:
        if is_member(First(L),Tail(L)):
            print(L)
            return Make_set(Tail(L))
        else:
            return konso(First, Make_set(Tail(L)))
L=[0,1,1,2,3,3,4,5,6,7,8,9]
print(Make_set(L))

def is_set(L):
    if is_empty(L):
        return False
    elif is_member(First(L), Tail(L)):
        return False
    else:
        return Is_set(Tail(L))

def Subset(H1,H2):
    if is_empty(H1):
        return True
    elif not is_member(First(H1,H2)):
        return False
    else:
        return Subset(Tail(H1),H2)

def is_intersect(H1,H2):
    if is_empty(H1)and is_empty(H2):
        return False
    elif not is_empty(H1) and is_empty(H2):
        return False
    elif is_empty(H1) and not is_empty(H2):
        return True
    else:
        return is_intersect(Tail(H1),H2)
    
def make_intersect(H1,H2):
    if is_empty(H1) and is_empty(H2):
        return []
    elif not is_empty(H1) and is_empty(H2):
        return []
    elif is_empty(H1) and not is_empty(H2):
        return []
    else:
        if is_member(First(H1),H2):
            return konso(First(H1),make_intersect(Tail(H1),H2))
        else:
            return make_intersect(Tail(H1),H2)

def make_union(H1,H2):
    if is_empty(H1) and is_empty(H2):
        return []
    elif not is_empty(H1) and is_empty(H2):
        return H1
    elif is_empty(H1) and not is_empty(H2):
        return H2
    else:
        if is_member(First(H1),H2):
            return make_union(Tail(H1),H2)
        else:
            return konso (First(H1),make_union(Tail(H1),H2))
