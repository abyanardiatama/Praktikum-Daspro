#NIM         : 24060120140161
#Nama        : Abyan A.
#Deskripsi   : Menghitung list dan set (himpunan) menggunakan operasi rekursif
#Tanggal     : 10 November 2020
#DASAR LIST
def konso(x,L):
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
def is1Elmt(L):
    return NbElmt(L)==1
def Rember(x,L):
    if is_empty(L):
        return []
    else:
        if First(L)==x:
            return Tail(L)
        else:
            return konso(First(L),Rember(x,Tail(L)))
        
def MultiRember(x,L):
    if is_empty(L):
        return []
    else:
        if First(L)==x:
            return MultiRember(x,Tail(L))
        else:
            Konso(First(L),MultiRember(x,Tail(L)))
def MakeSet(L):
    if is_empty(L):
        return []
    elif is_member(First(L),Tail(L)):
        return Rember(First(L),MakeSet(Tail(L)))
    else:
        return konso(First(L),MakeSet(Tail(L)))

#0 #DONE
#DEFSPEK
#NbVokal : list of char --> integer
#NbVokal(l) menghitung banyak elemen vokal dalam list
#REALISASI
def Nba(L):
    if is_empty(L):
        return 0
    else:
        if First(L)=='a':
            return 1 + Nba(Tail(L))
        else:
            return Nba(Tail(L))
def Nbi(L):
    if is_empty(L):
        return 0
    else:
        if First(L)=='i':
            return 1 + Nbi(Tail(L))
        else:
            return Nbi(Tail(L)) 
def Nbu(L):
    if is_empty(L):
        return 0
    else:
        if First(L)=='u':
            return 1 + Nbu(Tail(L))
        else:
            return Nbu(Tail(L))
def Nbe(L):
    if is_empty(L):
        return 0
    else:
        if First(L)=='e':
            return 1 + Nbe(Tail(L))
        else:
            return Nbe(Tail(L))
def Nbo(L):
    if is_empty(L):
        return 0
    else:
        if First(L)=='o':
            return 1 + Nbo(Tail(L))
        else:
            return Nbo(Tail(L))
def NbVokal(L):
    return Nba(L)+ Nbi(L) + Nbu(L) + Nbe(L) + Nbo(L)
#APLIKASI
L=['i','n','f','o','r','m','a','t','i','k','a']
L2=['j','a','y','a']
L3=['u','n','d','i','p']
print(NbVokal(L))
print(NbVokal(L2))
print(NbVokal(L3))

#1 #DONE
#SumElmt : list of integer --> integer
#SumElmt(L) menghasilkan jumlah semua elemen dalam list
#REALISASI
def SumElmt(L):
    if NbElmt(L)== 0:
        return 0
    else:
        if isinstance(First(L),int):
            return First(L) + SumElmt(Tail(L))
        else:
            return SumElmt(Tail(L))
#APLIKASI
L=[1,2,3,4,5]
L2=[43,56,3,76,3]
L3=[45,34,6,34]
print(SumElmt(L))
print(SumElmt(L2))
print(SumElmt(L3))

#2 #DONE
#KEMUNCULAN MAKSIMUM versi-2
#maxNb : list of integer --> <integer, integer>
#maxNb(Li) menghasilkan <nilai maksimum, kemunculan nilai maksimum> dari suatu list integer Li; <m,n> = m adalah maks x dari n
#          occurence m dalam list
#
#max : list of integer --> integer
#max(Li) menghasilkan nilai maksimum dari elemen suatu list integer Li
#
#Vmax : list of integer --> integer
#Vmax(Li) adalah NbOcc(max(Li),Li) yaitu banyaknya kemunculan nilai maksimum dari
#         Li, dengan aplikasi terhadap NbOcc(max(Li),Li)
#
#NbOcc : integer, list of integer --> integer > 0
#NbOcc(X,Li) yaitu banyaknya kemunculan nilai X pada Li
#REALISASI
def MaxNb(Li):
    for x in range(len(Li)-1):
        if Li[0] < Li[1]:
            del Li[0]
        elif Li[0] > L[1]:
            del Li[1]
        else:
            continue
    return (len(Li),Li[0])

def Max(L):
    if is1Elmt(L):
        return L[0]
    else:
        return max(L)
def NbOcc(x,L):
    if is1Elmt(L):
        if First(L)==x:
            return 1
        else:
            return 0
    else:
        if First(L)==x:
            return 1 + NbOcc(x,Tail(L))
        else:
            return 0 + NbOcc(x,Tail(L))
def Vmax(L):
    return NbOcc(Max(L),L)
#APLIKASI
L=[34,56,3,67,6,43,865]
print(Max(L))
print(Vmax(L))
print(MaxNb(L))
print(NbOcc(3,L))

#3
#LPrime(L) : list of integer --> list
#LPrime(L) menghasilkan list baru yang dimana isinya hanya bilangan prima
#REALISASI
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
    
def LPrime(L):
    if is_empty(L):
        return []
    else:
        if IsPrime(First(L)):
            return konso(First(L),LPrime(Tail(L)))
        else:
            return Rember(First(L),LPrime(Tail(L)))
def IsListPrime(L):
    if is_atom(L): 
            if IsPrime(First(L))or is_empty(L):
                return IsListPrime(Tail(L))
    else:
        False

L=[34,56,65,34,56,23]
L2=[17,45,43,65,78,34,214]
L3=[123,456,789,800]
print(LPrime(L))
print(LPrime(L2))
print(LPrime(L3)) 

#4
#InsertAfter: list --> list
#InsertAfter(L,x,e) menghasilkan list baru dimana menambahkan elemen x setelah elemen e 
#REALISASI
def InsertAfter(L,x,e):
    if is_empty(L):
        return konso(x,L)
    else:
        if First(L)==e:
            return konso(First(L),konso(x,Tail(L)))
        else:
           return konso(First(L),InsertAfter(Tail(L),x,e))

L=[1,3,4]
L2=[5,7,8]
L3=[9,10,12]
print(InsertAfter(L,2,1))
print(InsertAfter(L2,6,5))
print(InsertAfter(L3,11,10))

#5
#MakeMinus: 2 set --> set
#MakeMinus(H1,H2) membuat set baru dimana anggota H1 yang BUKAN merupakan anggota H2
def MakeMinus(H1,H2):
    if is_empty(H1):
        return []
    else:
        if is_member(First(H1),H2):
            return Rember(First(H1),MakeMinus(Tail(H1),H2))
        else:
            return konso(First(H1),MakeMinus(Tail(H1),H2))
H1=[34,56,45,980,59,257]
H2=[324,567,6234,45,354]
H3=[34,56,45,980,59,354]
print(MakeMinus(H1,H2))
print(MakeMinus(H1,H3))
print(MakeMinus(H2,H3))

#6
#MakeKomplemen: 2 set --> set
#MakeKomplemen(H1,H2)   membuat set baru yang anggotanya adalah anggota semua anggota H1 dan H2
#                       tetapi bukan interseksi keduanya
def Komplemen1(H1,H2):
    if is_empty(H1):
        return []
    else:
        if is_member(First(H1),H2):
            return Rember(First(H1),Komplemen1(Tail(H1),H2))
        else:
            return konso(First(H1),Komplemen1(Tail(H1),H2))
def Komplemen2(H2,H1):
    if is_empty(H2):
        return []
    else:
        if is_member(First(H2),H1):
            return Rember(First(H2),Komplemen2(Tail(H2),H1))
        else:
            return konso(First(H2), Komplemen2(Tail(H2),H1))
def MakeKomplemen(H1,H2):
    a=Komplemen1(H1,H2)
    b=Komplemen2(H2,H1)
    return MakeSet(a+b)
H1=[1,2,3,4,5,6]
H2=[32,4,5,43,7,3]
H3=[243,32,43,5,45,23]
print(MakeKomplemen(H1,H2))
print(MakeKomplemen(H2,H1))
print(MakeKomplemen(H1,H3))        

