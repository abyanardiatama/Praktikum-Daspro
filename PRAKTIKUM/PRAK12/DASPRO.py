"""
NIM         : 24060120140161
Nama        : Abyan A.
Deskripsi   : Menyelesaikan perhitungan Tree menggunakan operasi rekursif
Tanggal     : 23 November 2020
"""

#DASAR TREE
class PohonBiner:
    def __init__(self,A,L,R):
        self.A = A #Akar
        self.L = L #Left
        self.R = R #Right
def Akar(P):
    return P.A
def Left(P):
    return P.L
def Right(P):
    return P.R
def MakePB(A,L,R): #PohonBiner
    return PohonBiner(A,L,R)
###############################################################################################
def IsTreeEmpty(P):
    if P == None:
        return True
    else:
        return False
    
def IsOneElmtPB(P):
    if not IsTreeEmpty(P) and IsTreeEmpty(Right(P))and IsTreeEmpty(Left(P)):
        return True
    else:
        return False
###############################################################################################    
def IsUnerLeftPB(P): #P mengandung sub pohon kiri
    if not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
        return True
    else:
        return False
def IsUnerRightPB(P): #P mengandung sub pohon kanan
    if not IsTreeEmpty(P) and IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P)):
        return True
    else:
        return False
###############################################################################################
def IsExistLesftPB(P): #P mengandung sub pohon kanan
    if not IsTreeEmpty(P) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False
def IsExistRightPB(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)):
        return True
    else:
        return False
###############################################################################################    
def RepPrefixPB(P):
    if IsOneElmtPB(P):
        return [Akar(P)]
    else:
        if(IsBinerPB(P)):
            return [Akar(P)] + RepPrefix(Left(P)) + RepPrefix(Right(P))
###############################################################################################
def IsBiner(P):
    if not IsTreeEmpty(P) and not IsTreeEmpty(Right(P)) and not IsTreeEmpty(Left(P)):
        return True
    else:
        return False
###############################################################################################
def NbElmt(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmtPB(P):
        return 1
    else:
        if IsBiner(P):
            return NbElmt(Left(P)) + 1 + NbElmt(Right(P))
        elif IsUnerLeftPB(P):
            return NbElmt(Left(P)) + 1
        elif IsUnerRightPB(P):
            return NbElmt(Right(P)) + 1
        else:
            return 0
###############################################################################################
def NbDaunPB(P):
    if IsTreeEmpty(P):
        return 0
    elif IsOneElmtPB(P):
        return 1
    else:
        if IsBiner(P):
            return NbDaunPB(Left(P)) + NbDaunPB(Right(P))
        elif UnerLeftPB(P):
            return NbDaunPB(Left(P))
        elif IsUnerRight(P):
            return NbDaunPB(Right(P))
        else:
            return 0

###############################################################################################
#APLIKASI
P   =   MakePB(1,MakePB(2,None,None),MakePB(3,None,None))

P1  =   MakePB(
        2,
        MakePB(7,MakePB(2,None,None),MakePB(12,None,None)),
        MakePB(5,MakePB(6,None,None),MakePB(9,None,None))
        )

P2  =   MakePB(2,None,None)

P3  =   None

print("\n====IsTreeEmpty====")
print(IsTreeEmpty(P3))
print(IsTreeEmpty(P))

print("\n====NbElmt====")
print(NbElmt(P1))

print("\n====NbDaun====")
print(NbDaunPB(P1))

