# =====================
# Author : BenhardSim
# =====================

def NBelmt(L):
    if(len(L) == 0):
        return 0
    else:
        return 1 + NBelmt(L[1:])

def SumElet(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + SumElet(L[1:])

def isList(LOL):
    if type(LOL) == list:
        return True
    else:
        return False

def isAtom(LOL):
    if(isList(LOL)):
        return NBelmt(LOL) == 1
    else:
        return True

def hasilJual(LoL):
    if len(LoL) == 0:
        return 0
    elif isAtom(LoL[0]):
        if LoL[0]%2 == 0:
            return LoL[0]*4000 + hasilJual(LoL[1:])
        else:
            return LoL[0]*3000 + hasilJual(LoL[1:])
    elif isList(LoL[0]):
        if(SumElet(LoL[0])%2 == 0):
            return SumElet(LoL[0])*2000 + hasilJual(LoL[1:])
        else:
            return SumElet(LoL[0])*1000 + hasilJual(LoL[1:])

print(hasilJual([2,3,[1,4],[2,2],9]))
print(hasilJual([2,3,[1,4],[2,2],9,[2,1,3],3]))
print(hasilJual([2,1,[1,4],8]))
print(hasilJual([[1,4],2,[3,4],[0,2],9]))
print(hasilJual([2,3,6]))
