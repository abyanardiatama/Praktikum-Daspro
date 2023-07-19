def Day(D):
    return D[0]

def Month(D):
    return D[1]

def Year(D):
    return D[2]

def MakeDate(Hr, Bln, Thn):
    return [Hr, Bln, Thn]

def IsKabisat(a):
    return a % 4 == 0 and a % 100 != 0 or a % 400 == 0

def Yesterday(D):
    if(Day(D) == 1):
        if(Month(D) in [12, 5, 7, 8, 10]):
            return MakeDate(30, Month(D) - 1, Year(D))
        elif(Month(D) == 3):
            if(IsKabisat(Year(D))):
                return MakeDate(29, 2, Year(D))
            else:
                return MakeDate(28, 2, Year(D))
        elif(Month(D) in [2, 4, 6, 9, 11]):
            return MakeDate(31, Month(D) - 1, Year(D))
        elif(Month(D) == 1):
            return MakeDate(31, 12, Year(D) - 1)
    else:
        return MakeDate(Day(D) - 1, Month(D), Year(D))

def Nextday(D):
    if(Month(D) in [1, 3, 5, 7, 8, 10, 12]):
        if(Day(D) < 31):
            return MakeDate(Day(D) + 1, Month(D), Year(D))
        else:
            if(Month(D) == 12):
                return MakeDate(1, 1, Year(D) + 1)
            else:
                return MakeDate(1, Month(D) + 1, Year(D))
    elif(Month(D) in [4, 6, 9, 11]):
        if(Day(D) < 30):
            return MakeDate(Day(D) + 1, Month(D), Year(D))
        else:
            return MakeDate(1, Month(D) + 1, Year(D))
    else:
        if(Day(D) < 28 or (IsKabisat(Year(D)) and Day(D) < 29)):
            return MakeDate(Day(D)+1, Month(D), Year(D))
        else:
            return MakeDate(1, Month(D) + 1, Year(D))
    
def NextNday(D, N):
    if(N == 0):
        return D
    else:
        return NextNday(Nextday(D), N-1)

def dpm(B):
    match B:
        case 1:
            return 1
        case 2:
            return 32
        case 3:
            return 60
        case 4:
            return 91
        case 5:
            return 121
        case 6:
            return 152
        case 7:
            return 182
        case 8:
            return 213
        case 9:
            return 244
        case 10:
            return 274
        case 11:
            return 305
        case 12:
            return 335

def HariKe1900(D):
    if(Month(D) > 2 and IsKabisat(Year(D))):
        return ((Year(D) - 1900) * 365) + dpm(Month(D)) + Day(D) - 1 + 1
    else:
        return ((Year(D) - 1900) * 365) + dpm(Month(D)) + Day(D) - 1 + 0

def IsEqD(D1, D2):
    return HariKe1900(D1) == HariKe1900(D2)

def IsBefore(D1, D2):
    return HariKe1900(D1) < HariKe1900(D2)
        
def IsAfter(D1, D2):
    return HariKe1900(D1) > HariKe1900(D2)


print(Yesterday(MakeDate(1,3,2020)))
print(Nextday(MakeDate(29,2,2020)))
print(NextNday(MakeDate(1,1,2020), 400))
print(HariKe1900(MakeDate(1,1,1901))) #Pada harike1900 batasnya hanya sampai 366 (sampai tanggal 1 januari 1901) mengikuti diktat
print(IsEqD(MakeDate(1,1,1901), MakeDate(2, 1, 1901)))
print(IsBefore(MakeDate(30,12,1900), MakeDate(31, 12, 1900)))
print(IsAfter(MakeDate(30,12,1900), MakeDate(29, 12, 1900)))
print(IsKabisat(1904))