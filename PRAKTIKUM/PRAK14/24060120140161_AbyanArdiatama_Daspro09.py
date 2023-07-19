"""
NIM             : 24060120140161
Nama            : Abyan Ardiatama
Deskripsi       : Kenang-kenangan:)
Tanggal         : 8 Desember 2020
"""
from Dasar_List import*
from Dasar_Tree import*

#LIST#
L1 = []
L2 = [1,2,3]
L3 = [1, [2,3], [4]]
L4 = ['u', 'n', 'd', 'i' 'p']

#MATRIX#
M2 = [[1,2,3],[4,5,6],[7,8,9]]
M1 = [
           [1,2,3],
           [4,5,6],
           [7,8,9]
        ]

#SET#
H1 = [4, 5, 6]
H2 = []

#TREE#
P1 = [1,
            [2,
                [3, [], []],
                [4, [], []]
            ],
            [5, [], []]
        ]
P2= [2, [], []]


"""""""LIST"""""""
"""1"""
# DefSpek
# SumElmtX : Integer, List of integer --> integer
# SumElmtX (X, L) menjumlahkan nilai elemen list tanpa elemen bernilai X
# L = [1,2,3,4,5]
# Aplikasi : SumElmtX(5, L) --> 10
def SumElmtX(X,L):
    if IsEmpty(L):
        return 0
    else:
        if First(L)== X:
            return SumElmtX(X,Tail(L))
        else:
            return First(L)+SumElmtX(X,Tail(L))
L5 = [1,2,3,4,5]
print("\n====SumElmtX====")
print(SumElmtX(5,L2))
print(SumElmtX(3,L5))

"""2"""
# DefSpek 
# MaxList : List of integer --> Integer
# MaxList(L) menghasilkan nilai elemen terbesar dari list L
# L = [2,4,5,1]
# Aplikasi : MaxList(L) --> 5
# Hint : Untuk memudahkan, buat fungsi untuk mengecek nilai maksimum
def MaxList(L):
    if IsEmpty(L):
        return 0
    elif NbElmt(L)==1:
        return First(L)
    else:
        if First(L)<First(Tail(L)) :
            return MaxList(Tail(L))
        else:
            return MaxList(Rember(First(Tail(L)),L))

L5 = [1,2,3,4,5]
L6 = [2,4,5,1]
print("\n====MaxList====")
print(MaxList(L5))
print(MaxList(L6))

"""3"""
# DefSpek 
# MinList : List of integer --> Integer
# MinList(L) menghasilkan nilai elemen terkecil dari list L
# L = [2,4,5,1]
# Aplikasi : MinList(L) --> 1
def MiniList(L):
    if IsEmpty(L):
        return 0
    elif NbElmt(L)==1:
        return First(L)
    else:
        if First(L)<First(Tail(L)):
            return MiniList(Rember(First(Tail(L)),L))
        else:
            return MiniList(Tail(L))

print("\n====MiniList====")
print(MiniList(L5))
print(MiniList(L6))

"""4"""
# DefSpek
# UraikanListOfList : List of list --> List
# UraikanListOfList(L) menghasilkan hasil penguraian dari List of list L menjadi list biasa
# L = [1, [2,3], 4, [5]]
# Aplikasi : UraikanListOfList(L) --> [1, 2, 3, 4, 5]
def UraikanListofList(L):
    if IsEmpty(L):
        return []
    elif type(First(L))!= list:
        return Konso(First(L),UraikanListofList(Tail(L)))
    elif type(First(L))==list:
        return First(L) + UraikanListofList(Tail(L))

L7 = [1, [2,3], 4, [5]]
print("\n====UraikanListoflist====")
print(UraikanListofList(L3))
print(UraikanListofList(L7))

"""5"""
# DefSpek
# ListMaxMin : List of integer --> List
# ListMaxMin(L) membuat List dengan anggotanya hanya 2 elemen yaitu elemen terbesar dan terkecil dari list L
# L = [4, 2, 5, 3, 7, 1]
# Aplikasi : ListMaxMin(L) ---> [1, 7] 
def ListMaxMin(L):
    return [MiniList(L)]+ [MaxList(L)]

L8 = [4, 2, 5, 3, 7, 1]
print("\n====ListMaxMin====")
print(ListMaxMin(L2))
print(ListMaxMin(L8))

"""6"""
# DefSpek
# SetElmtXzero : Integer, list of integer --> list of integer
# SetElmtXzero(L,3) menghasilkan list baru yang mengganti setiap elemen x menjadi 0
# L = [1, 2, 3, 4, 5]
# Aplikasi : SetElmtXzero(L,3) --> [1, 2, 0, 4, 5]
def SetElmtXzero(L,X):
    if IsEmpty(L):
        return []
    else :
        if First(L)== X:
            return SetElmtXzero(Konso(0,Rember(First(L),L)),X)
        else:
            return Konso(First(L),SetElmtXzero(Tail(L),X))

print("\n====SetElmtXzero====")
print(SetElmtXzero(L2,3))
print(SetElmtXzero(L8,7))

"""7"""
# DefSpek
# XPos : List of char --> Integer
# XPos(L,X) menghasilkan posisi index dari char X yang dicari
# L = ['j', 'a', 'y', 'a']
# Aplikasi : XPos(L,'a') --> 1 
# Hint : Index dimulai dari 0. Huruf 'a' pada contoh di atas berada pada POSISI INDEX ke-1 dari list L
#          Jika ada lebih dari satu karakter yang sama, return index karakter pertama yang ketemu
def XPos(L,X):
    if IsEmpty(L):
        return 0
    elif IsMember(L,X):
        if First(L) == X:
            return 0
        elif First(Tail(L))==X:
            return 1
        else:
            return 1 + XPos(Tail(L),X)
    else:
        return False

L10 = ['j', 'a', 'y', 'a']
print("\n====XPos====")
print(XPos(L4,'d'))
print(XPos(L10,'y'))

"""8"""
# DefSpek
# SortMax(L) : list of integer --> list of integer
# SortMax(L) menghasilkan list baru dimana mengurutkan elemen dari yang terbesar ke terkecil
# Hint : Ada di diktat, tinggal ubah sedikit
def SortMax(L):
    if IsEmpty(L):
        return []
    else:
        return [MaxList(L)] + SortMax(Rember(MaxList(L),L))

print("\n====SortMax====")
print(SortMax(L5))
print(SortMax(L8))

"""""""SET"""""""
"""9"""
# DefSpek
# RemberAll : Set --> Empty Set
# RemberAll(H) menghapus semua elemen pada set H
# H = [1, 2, 3, 4]
# Aplikasi : RemberAll(H) --> []
# Hint : Jangan langsung return []
def RemberAll(H):
    if IsEmpty(H):
        return []
    else:
        return RemberAll(Rember(First(H),H))

H3 = [1, 2, 3, 4]
print("\n====RemberAll====")
print(RemberAll(H2))
print(RemberAll(H3))

"""""""TREE"""""""
"""10"""
# DefSpek
# TinggiPohon : Binary Tree --> Integer
# TinggiPohon(P) menghasilkan tinggi dari pohon P (Tinggi pohon dimulai dari 1)
#                4              --Level 1
#             /     \
#           2         5         --Level 2
#         /
#       1                       --Level 3
# Aplikasi : TinggiPohon(P) --> 3 
# Hint : Hati-hati dengan perbedaan tinggi Left(P) dan Right(P)
def TinggiPohon(P):
    if NbElmt(Left(P))>NbElmt(Right(P)):
        return NbElmt(Left(P))
    else:
        return NbElmt(Right(P))

P3  =   MakePB(4,
        MakePB(2,MakePB(1,None,None),None),
        MakePB(5,None,None))
P4  =   MakePB(4,
        MakePB(2,MakePB(1,None,None),None),
        MakePB(5,None,MakePB(6,None,None)))
print("\n====TinggiPohon====")
print(TinggiPohon(P3))
print(TinggiPohon(P4))

"""11"""
# DefSpek
# IsBalanceTree : Binary Tree  --> Boolean
# IsBalanceTree(P) mengecek apakah pohon P merupakan balance tree
#                4              
#             /     \
#           2         5         
#         /             \
#       1                 6       
# Aplikasi : IsBalanceTree(P) --> True
# Hint : Balance tree bernilai true ketika selisih tinggi pohon Right dan Left tidak lebih dari 1
#        : ATAU selisih banyaknya node Right dan Left tidak lebih dari 1
def IsBalanceTree(P):
    if NbElmtPB(Left(P))-NbElmtPB(Right(P))<=1 or NbElmtPB(Right(P))-NbElmtPB(Left(P))<=1:
        return True
    else:
        return False

print("\n====IsBalanceTree====")
print(IsBalanceTree(P3))
print(IsBalanceTree(P4))
            
"""12"""
# DefSpek
# Terkiri : Binary Search Tree --> Node dalam integer
# Terkiri(P) menghasilkan node terkiri dari pohon P
#                7              
#             /     \
#           2         8         
#         /   \      /
#       1       3  6
#                  /
#                 5               
# Aplikasi : Terkiri(P) --> 1
# Hint : Node terkiri selalu node paling kecil dari BinarySearchTree
def Terkiri(P):
    if IsOneElmtPB(P):
        return Akar(P)
    elif IsExistLeftPB(P):
        return Terkiri(Left(P))

P5  =   MakePB(7,
        MakePB(2,MakePB(1,None,None),MakePB(3,None,None)),
        MakePB(8,MakePB(6,MakePB(5,None,None),None),None))
print("\n====Terkiri====")
print(Terkiri(P4))
print(Terkiri(P5))

"""13"""
# DefSpek
# IsSkewRight : Binary Tree  --> Node atau integer
# IsSkewRight(P) mengecek apakah pohon P condong kanan 
# P1
#                7              
#                  \
#                    8         
#                      \
#                        9
#                         \ 
#                           10     
# Aplikasi : IsSkewRight(P1) --> True
# P2
#                7              
#             /     \
#           2         8         
#         /   \      /
#       1       3  6
#                  /
#                 5    
# Aplikasi : IsSkewRight(P2) --> False
def IsSkewRight(P):
    if IsUnerRightPB(P)or IsUnerLeftPB(P):
        return True
    else:
        return False

P6  =   MakePB(7,
        None,
        MakePB(8,MakePB(9,MakePB(10,None,None),None),None))
P7  =   MakePB(7,
        MakePB(2,MakePB(1,None,None),MakePB(3,None,None)),
        MakePB(8,MakePB(6,MakePB(5,None,None),None),None))

print("\n====IsSkewRight====")
print(IsSkewRight(P6))
print(IsSkewRight(P7))

"""""""SOAL BONUS"""""""
"""Buat latihan aja, nggak usah dikumpulin"""
"""999"""
# DefSpek
# ReversePohon : Binary Tree  --> Tree
# ReversePohon(P) menghasilkan pohon P yang sudah di reverse
# P = [1,
#        [2,
#            [4, 
#                [8, [], []], 
#                [9, [], []]
#            ],
#            [5, [], []]
#       ],
#        [3, 
#            [6, [], []], 
#            [7, [], []]
#        ]
#      ]

#                1              
#             /      \
#           2          3         
#         /   \      /    \
#       4      5   6      7    
#      / \
#     8   9      

# Aplikasi : ReversePohon(P) --> 
# P = [1,
#           [3,
#               [7, [], []],
#               [6, [], []]
#            ],
#           [2, 
#               [5, [], []], 
#                   [4, 
#                        [9, [], []], 
#                        [8, [], []]
#                   ]
#            ]
#       ]    

#                1              
#             /      \
#           3          2         
#         /   \      /    \
#       7      6   5      4    
#                           / \
#                          9   8       
def ReversePohon(P):
    return MakePB(P[0],P[-1],P[1])
print("\n====ReversePohon====")
print(ReversePohon(P3))
