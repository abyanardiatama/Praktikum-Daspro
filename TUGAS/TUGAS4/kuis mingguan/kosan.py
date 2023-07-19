def kamarkos(g,l,k):
    return [g,l,k]

def gedung(kos):
    return kos[0]
def lantai(kos):
    return kos[1]
def kamar(kos):
    return kos[2]

def lokasigedung(kos):
    if(gedung(kos) == 1):
        return 'A'
    elif(gedung(kos) == 2):
        return 'B'
    elif (gedung(kos) == 3):
        return 'C'
    elif (gedung(kos) == 4):
        return 'D'
    elif (gedung(kos) == 5):
        return 'E'
    elif (gedung(kos) == 6):
        return 'F'
    elif (gedung(kos) == 7):
        return 'G'
    elif (gedung(kos) == 8):
        return 'H'
    elif (gedung(kos) == 9):
        return 'I'

def lokasilengkap(kos):
    print ("Gedung " + lokasigedung(kos))
    print ("Lantai " + str(lantai(kos)))
    print ("Nomor " + str(kamar(kos)))
                
x = input()
list(x)
kamar1 = kamarkos(int(x[0]),int(x[1]),int(x[2]))
lokasilengkap(kamar1)
