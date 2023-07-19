"""
NIM         : 24060120140161
Nama        : Abyan A.
Deskripsi   : Menyelesaikan perhitungan Tree menggunakan operasi rekursif
Tanggal     : 1 Desember 2020
"""
from Dasar_Tree import*
from Dasar_List import*

###########################################################################################################################################################################  
def BSearchX(P,X):
    if IsTreeEmpty(P):
        return False
    else:
        if Akar(P)== X:
            return True
        elif Akar(P) != X :
            return BSearchX(Right(P),X)
        else:
            return BSearchX(Left(P),X)
    
def AddX(P,X):
    if IsTreeEmpty(P):
        return MakePB(X,None,None)
    elif X < Akar(P):
        return MakePB(Akar(P),Left(P),AddX(Right(P),X))
    else:
        return MakePB(Akar(P),AddX(Left(P),X),Right(P))
###########################################################################################################################################################################      
#Deskripsi : {MakeBinSearchTree(L) menghasilkan pohon Binary Search Tree P yang elemennya berasal dari list L yang unik}
#MakeBinSearchTree(L): list of element --> Pohon Biner
def BinSearchTree(L,P):
    if(IsEmpty(L)):
        return P
    else:
        return BinSearchTree(Tail(L), AddX(P, First(L)))
def MakeBinSearchTree(L):
    return BinSearchTree(L,P)
###########################################################################################################################################################################  
#DEFSPEK
#Deskripsi : {DelBTree(P,X) mengahsilkan sebuah pohon binary search P tanpa node yang bernilai X, dimana X adalah salah satu node dari Binary Search Tree}
#DelBTree(P,X) : BinSearchTree tidak kosong, elemen --> Pohon Biner
def Terkiri(P):
    if IsOneElmtPB(P):
        return Akar(P)
    elif IsExistLeftPB(P):
        return Terkiri(Left(P))
def DelBTree(P, X):
    if(IsTreeEmpty(P)):
        return P
    else:
        if(Akar(P) == X):
            if(IsOneElmtPB(P)):
                return []
            elif(IsUnerLeft(P)):
                return Left(P)
            elif(IsUnerRight(P)):
                return Right(P)
            else:
                if(IsExistRight(P)):
                    if(IsUnerRight(P)):
                        return MakePB(Akar(Right(P)), Left(P), Right(Right(P)))
                    else:
                        return MakePB(Terkiri(Right(P)), Left(P), DelBTree(Right(P), Terkiri(Right(P))))
                else:
                    return MakePB(Akar(Left(P)), Right(Left(P)), Right(P))
        else:
            if(X > Akar(P)):
                return MakePB(Akar(P), Left(P), DelBTree(Right(P), X))
            else:
                return MakePB(Akar(P), DelBTree(Left(P), X), Right(P))
###########################################################################################################################################################################  
#Deskripsi : {Build Balance Tree(L,n) menghasilkan sebuah balance tree dengan n node, nilai tiap node berasal dari list}
#Build Balance Tree : list of node, integer --> BinBalTree
import math 
def BuildBalanceTree(L):
    L =sorted(L)
    if IsEmpty(L):
        return L
    else:
        mid =(len(L))//2
        Akar=L[mid]
        Left=BuildBalanceTree(L[:mid])
        Right=BuildBalanceTree(L[mid+1:])    
        return MakePB(Akar,Left,Right)
    
###########################################################################################################################################################################  
#APLIKASI
PP =   MakePB(
        30,
        MakePB(20,MakePB(15,MakePB(10,MakePB(5,None,None),None),None), MakePB(25,None,None)),
        MakePB(40,None,MakePB(50,MakePB(45,None,None),None)))

P   =   MakePB(1,MakePB(3,None,None),MakePB(5,None,None))

print("\n====BSearchX====")
print(BSearchX(PP,40))
print("\n====AddX====")
print(AddX(PP,31))
print("\n====MakeBinSearchTree====")
print(MakeBinSearchTree([2,4,6]))
print("\n====DelBTree====")
print(DelBTree(PP,45))
print("\n====BuildBalanceTree====")
print(BuildBalanceTree([1,2,3,4,5,6,7]))

