"""
NIM         : 24060120140126
Nama        : Wildan Kamal Allam
Deskripsi   : 
Tanggal     :
"""
#0
#DefSpek
#NbVokal : list of char --> integer
#NbVokal(l) menghitung banyak elemen vokal dalam list
def Nbvokal(l):
    vokal = ['a', 'i', 'u', 'e', 'o']
    jumlvokal = ['']
    for character in l:
        if character in vokal:
            jumlvokal += character
    return len(jumlvokal)
             
#1
#SumElmt : list of integer --> integer
#SumElmt(L) menghasilkan jumlah semua elemen dalam list
def sumelmnt(L):
    x = sum(L)
    return x
#2
#KEMUNCULAN MAKSIMUM versi-2
#maxNb : list of integer --> <integer, integer>
#maxNb(Li) menghasilkan <nilai maksimum, kemunculan nilai maksimum> dari suatu list integer Li; <m,n> = m adalah maks x dari n
#          occurence m dalam list
#
def maxNb(Li):
    for x in range(len(Li)-1):
            if Li[0] < Li[1]:
                del Li[0]
            elif Li[0] > Li[1]:
                del Li [1]
            else:
                continue
    return (len(Li),Li[0])
#max : list of integer --> integer
#max(Li) menghasilkan nilai maksimum dari elemen suatu list integer Li
#
def max(Li):
    for x in range(len(Li)-1):
        if Li[0] < Li[1]:
            del Li[0]
        else:
            del Li [1]
    return Li
#Vmax : list of integer --> integer
#Vmax(Li) adalah NbOcc(max(Li),Li) yaitu banyaknya kemunculan nilai maksimum dari
#         Li, dengan aplikasi terhadap NbOcc(max(Li),Li)
#
def Vmax(Li):

    for x in range(len(Li)-1):
        if Li[0] < Li[1]:
            del Li[0]
        elif Li[0] > Li[1]:
            del Li [1]
        else:
            continue
    return len(Li)
#NbOcc : integer, list of integer --> integer > 0
#NbOcc(X,Li) yaitu banyaknya kemunculan nilai X pada Li
def NbOcc(X,Li):
   hadeh = Li.count(X)
   return hadeh

#3
#LPrime(L) : list of integer --> list
#LPrime(L) menghasilkan list baru yang dimana isinya hanya bilangan prima

def faktor(n,count):
    if(n == count):
        return 1
    elif(n % count == 0):
        return 1 + faktor(n,count+1)
    else:
        return faktor(n,count+1)
        
def IsPrime(n):
    if(faktor(n,1) == 2):
        return True
    else:
        return False

def LPrime (L):
    b=[]
    for x in range(len(L)):
        if IsPrime(L[x]):
            b.append(L[x])
    return b

#4
#InsertAfter: list --> list
#InsertAfter(L,x,e) menghasilkan list baru dimana menambahkan elemen x setelah elemen e
def InsertAfter(L,x,e):
    for i in range(len(L)-1):
        if L[i] == e:
            L.insert(i+1, x)
    return L

#5
#MakeMinus: 2 set --> set
#MakeMinus(H1,H2) membuat set baru dimana anggota H1 yang BUKAN merupakan anggota H2
def MakeMinus(H1,H2):
    adu = []
    for character in H1:
        if character not in H2:
            adu += character
    return adu

#6
#MakeKomplemen: 2 set --> set
#MakeKomplemen(H1,H2)   membuat set baru yang anggotanya adalah anggota semua anggota H1 dan H2
#                       tetapi bukan interseksi keduanya
def MakeKomplemen(H1,H2):
    return (sorted(set(H1+H2)))

l = ['z','a','n','k','o','k','u','n','a','t','e','n','s','h','i','n','o','t','e','e','z','e']
L = [1,7,7,0,1,3]
L1 = [1,9,7,0,1,3]
L2 = [2,5,1,9,7,3]
H1 = ['a','b','c','d','l','k','h']
H2 = ['a','f','c','d','i','o','p']









    
