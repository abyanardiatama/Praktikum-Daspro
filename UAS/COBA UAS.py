from Dasar_List import*
from Dasar_Tree import*
#==============================================================
print("==========No.1===========")
def max2(a,b):
    if a>b:
        return a
    else:
        return b
def min2(a,b):
    if a<b:
        return a
    else:
        return b
    
def max_list(L):
    if IsEmpty(L):
        return 0
    elif NbElmt(L)==1:
        return First(L)
    else:
        return max2(First(L),max_list(Tail(L)))
def min_list(L):
    if IsEmpty(L):
        return 0
    elif IsOneElmt(L):
        return First(L)
    else:
        return min2(First(L),min_list(Tail(L)))
L2=[9,2,5,1,4,-3,10,-9,1]
print("max_list=",max_list(L2))
print("min_list=",min_list(L2))
print("==========No.2===========")
def SumDaun(P):
    if IsOneElmtPB(P):
        return Akar(P)
    else:
        if IsBiner(P):
            return SumDaun(Left(P)) + SumDaun(Right(P))
        elif IsUnerLeftPB(P):
            return SumDaun(Left(P))
        else:
           return SumDaun(Right(P)) 
def SumNode(P):
    if IsOneElmtPB(P):
        return Akar(P)
    else:
        if IsBiner(P):
            return Akar(P) + SumNode(Left(P)) + SumNode(Right(P))
        elif IsUnerLeftPB(P):
            return Akar(P) + SumNode(Left(P))
        else:
            return Akar(P) + SumNode(Right(P))
P = MakePB(8,
           MakePB(3,
                  MakePB(1,None,None),MakePB(6,
                        MakePB(4,None,None),MakePB(7,None,None))),
           MakePB(10,None,
                  MakePB(14,
                         MakePB(13,None,None),None)))
print("SumDaun=",SumDaun(P))
print("SumNode=",SumNode(P))
print("==========3a===========")
def IsGenap(x):
    a = x%2==0
    if a:
        return True
    else:
        return False
def IsGanjil(y):
    b = y%2 != 0
    if b:
        return True
    else:
        return False
L1=[4,8,11,2,19,23,45,20]
def FilterListGenap(L):
    if IsEmpty(L):
        return []
    else:
        if IsGenap(First(L)):
            return Konso(First(L),FilterListGenap(Tail(L)))
        else:
            return FilterListGenap(Tail(L))
print("FilterList_Genap=",FilterListGenap(L1))

def FilterListGanjil(L):
    if IsEmpty(L):
        return []
    else:
        if IsGanjil(First(L)):
            return Konso(First(L),FilterListGanjil(Tail(L)))
        else:
            return FilterListGanjil(Tail(L))
print("FilterList_Ganjil=",FilterListGanjil(L1))

print("==========3b===========")
def FilterList_Genap(L):
    if L==[]:
        return []
    else:
        if L[0] % 2 == 0:
            return [L[0]] + FilterListGenap(L[1:])
        else:
            return FilterListGenap(L[1:])
print("Lambda_FilterList_Genap=",FilterList_Genap(L1))

def FilterList_Ganjil(L):
    if L==[]:
        return []
    else:
        if L[0] % 2 != 0:
            return [L[0]] + FilterListGanjil(L[1:])
        else:
            return FilterList_Ganjil(L[1:])
print("Lambda_FilterList_Ganjil=",FilterList_Ganjil(L1))
print("==========No.4===========")
def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        if First(L)==X:
            return True
        else:
            return IsMember(X,Tail(L))
def IsSubset(H1,H2):
    if IsEmpty(H1):
        return True
    else:
        if not IsMember(First(H1),H2):
            return False
        else:
            return IsSubset(Tail(H1),H2)
def Minus(H1,H2):
    if IsSubset(H1,H2):
        return []
    elif IsMember(First(H1),H2):
        return Minus(Tail(H1),H2)
    else:
        return Konso([First(H1)],Minus(Tail(H1),H2))
H   = [5,2,6,7,9,15]
H1  = [2,7,15]
print("Minus=",Minus(H,H1))
            
