#Nama File  : List.py
#Deskripsi  : Menghitung List 
#Pembuat    : Abyan A.
#Tanggal    : 3 November 2020

#DEFINISI DAN SPESIFIKASI
#NO1
#ElmtkeN : integer>=[] --> Element
#   {ElmtkeN(L) menghasilkan elemen ke N dari list L, N>=0, dan N<=banyak element list}

#NO2
#isX_ElmtkeN : element, integer>=0, List!=[] --> Boolean
#   {isX_ElmtkeN(N,L)bernilai True jika X adalah elemen ke-N list L, N>=0, dan N<=banyak elemen list}

#NO3
#is_inverse : 2 List --> Boolean
#   {is_inverse(L1,L2) bernilai True jika L2 adalah list dengan urutan terbalik dari L1}

#REALISASI
def konso(L,x):
    return [x]+L
def kons(L,x):
    return L + [x] 
def First(L):
    return L[0]
def Last(L):
    if L==[]:
        return False
    else:
        return L[-1]
def Head(L):
    if not L==[]:
        return L[:-1]
def Tail(L):
    if not L==[]:
        return L[1:]
def is_empty(L):
    if L==[]:
        return True
    else:
        return False
def NbElmt(L):
    if is_empty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
def is_member(x,L):
    if is_empty(L):
        return False
    else:
        if Last(L)==x:
            return True
        elif Last(L)!=x:
            return is_member(x,Head(L))

#NO1
def ElmtkeN(N,L):
    if N==1:
        return First(L)
    else:
        return ElmtkeN(N-1, Tail(L))

#NO2
def isX_ElmtkeN(X,N,L):
    if is_member(X,L):
        if N==1 and First(L) == X:
            return True
        elif N==1 and First(L) != X:
            return False
        else:
            return isX_ElmtkeN(X,N-1,Tail(L))
    else:
        return False

#NO3
def is_inverse(L1,L2):
    if NbElmt(L1)==NbElmt(L2):
        if is_empty(L1) and is_empty(L2):
            return True
        else:
            return First(L1)==Last(L2) and is_inverse(Head(L1),Tail(L2))
    else:
        return False

#APLIKASI
#NO1
L=[3,4,54,23,5,2]
print(ElmtkeN(2,L))
print(ElmtkeN(4,L))
print(ElmtkeN(3,L))
print(ElmtkeN(1,L))
print(ElmtkeN(6,L))

#NO2
L=[34,5,23,56,66,22]
print(isX_ElmtkeN(34,1,L))
print(isX_ElmtkeN(21,4,L))
print(isX_ElmtkeN(56,4,L))
print(isX_ElmtkeN(23,6,L))
print(isX_ElmtkeN(22,6,L))

#NO3
P=[34,454,6,45,54,56]
Q=[56,54,45,6,454,33]
R=[1,2,3,4,5]
S=[5,4,3,2,1]
print(is_inverse(P,Q))
print(is_inverse(R,S))
