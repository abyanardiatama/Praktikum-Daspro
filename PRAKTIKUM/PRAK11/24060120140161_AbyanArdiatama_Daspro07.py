"""
NIM         : 24060120140161
Nama        : Abyan A.
Deskripsi   : Menyelesaikan perhitungan List of List menggunakan operasi rekursif
Tanggal     : 18 November 2020
"""
"""Ex:
Matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
Matrix1 = [
              [1,2,3],
              [4,5,6],
              [7,8,9]
            ]
"""
#DASARLIST
def is_empty(L):
    return L==[]
def FirstL(L):
    if is_empty(L):
        return []
    else:
        return L[0]
def Konslo(L,S):
    return [L]+S
def Konsl(S,L):
    return S+[L]
def NbElmt(L):
    if is_empty(L):
        return 0
    else:
        return 1 + NbElmt(TailL(L))
def TailL(L):
    return L[1:]
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

# 1
# DefSpek
# NbEleX : elemen, list of list --> integer
# NbEleX (L,X) menentukan banyaknya X dalam list L
# L1 = [[4], 2, [3,4], 1, 4]
# aplikasi : NbEleX(L1,4) --> 3
def NbEleX(L,X):
    if is_empty(L)or L==[[]]:
        return 0
    else:
        if FirstL(L)==X:
            return 1 + NbEleX(TailL(L),X)
        elif is_list(FirstL(L)):
            if FirstL(FirstL(L))==X:
                return 1 + NbEleX(Konsl(TailL(FirstL(L)),TailL(L)),X)
            else:
                return NbEleX(Konsl(TailL(FirstL(L)),TailL(L)),X)
        elif is_atom(FirstL(L)):
            if FirstL(FirstL(L))==X:
                return 1 + NbEleX(TailL(L),X)
            else:
                return NbEleX(TailL(L),X)   
        else:
            return NbEleX(TailL(L),X)
#APLIKASI
L   = [[4], 2, [3,4], 1, 4]
L2  = [[5],[3,5,6],5,3,6]
L4  = [6,[56,3,6],[6],[3,5]]
print(NbEleX(L,4))
print(NbEleX(L2,5))
print(NbEleX(L4,7))

# 2
# DefSpek
# KaliMatrix : Integer, list of list dalam bentuk matrix --> list
# KaliMatrix (k, L) menghasilkan matrix dalama bentuk list
# yang telah dikali dengan suatu konstanta K
# L3 = [[1,2,3], [4,5,6], [7,8,9]]
# aplikasi : KaliMatrix(2, L3) --> [[2,4,6],[8,10,12],[14,16,18]]

def KaliMatrix(k,L):
    if is_empty(L):
        return []
    elif is_list(FirstL(L)) :   
        return Konslo(KaliMatrix(k,(FirstL(L))),KaliMatrix(k,TailL(L)))
    else:
        return Konslo((k*FirstL(L)),KaliMatrix(k,(TailL(L))))

#APLIKASI
L   =   [[1,2,3],[4,5,6],[7,8,9]]
L2  =   [[4,6],[3,7]]
L3  =   [[3,3],[5,6]]
print(KaliMatrix(2,L))
print(KaliMatrix(5,L2))
print(KaliMatrix(3,L3))

# 3
# DefSpek
# NbList : list of list --> integer
# NbList (L) menghitung jumlah list dalam list L
# L4 = [1, [2,3], [4]]
# L3 = [[5], [6], [7]]
# L2 = [8, 9, 10]
# aplikasi : NbList(L4) --> 2
#               NbList(L3) --> 3
#               NbList(L2) --> 0
def NbList(L):
    if is_empty(L):
        return 0
    else:
        if type(FirstL(L))==int:
            return 0 + NbList(TailL(L))
        elif is_list(FirstL(L)): 
            return 1 + NbList(TailL(L))
        elif is_atom(FirstL(L)):
            return 1 + NbList(TailL(L))
        else:
            return NbList(TailL(L))
#APLIKASI
L   =   [8, 9, 10]
L2  =   [1, [2,3], [4]]
L3  =   [[3],[4],[5],[2],[9],[43]]
print(NbList(L))
print(NbList(L2))
print(NbList(L3))

            
            
