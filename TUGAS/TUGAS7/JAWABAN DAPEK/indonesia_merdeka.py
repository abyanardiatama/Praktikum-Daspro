def NBelmt(L):
    if(len(L) == 0):
        return 0
    else:
        return 1 + NBelmt(L[1:])

def isList(LOL):
    if type(LOL) == list:
        return True
    else:
        return False

def isAtom(LOL):
    if(isList(LOL)):
        return False
    else:
        return True

def MaxList(L,maxNum):
    if len(L) == 0:
        return maxNum
    else:
        return MaxList(L[1:],max(L[0],maxNum))


def biaya(LOL,prajurit,ninja):
    if len(LOL) == 0:
        return (prajurit+ninja)*1000000
    elif isAtom(LOL[0]):
        return biaya(LOL[1:], max(LOL[0],prajurit) ,ninja)
    elif isList(LOL[0]):
        return biaya(LOL[1:], prajurit, ninja + MaxList(LOL[0],0))

print(biaya([[2,3,4,6],[1,1,3,9,2,7],3,1,[2,1],7,2,[4,4,6],1,[3,3]],0,0))
print(biaya([[2,3,4,6,7],[1,1,3,2,7],[5,2,1],[4,4,6],[3,3],1,2,3],0,0))
print(biaya([[2,3],[1,1,2],[1],[4,4],[3,3],4,4,1],0,0))
print(biaya([8,[5,2,3],[1,1,2],[1],[4,4],[3,3],4,4,1],0,0))
