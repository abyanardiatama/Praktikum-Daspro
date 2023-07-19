"""
NIM         :
Nama        :
Deskripsi   : 
Tanggal     :
"""
#0
#DefSpek
#NbVokal : list of char --> integer
#NbVokal(l) menghitung banyak elemen vokal dalam list

#1
#SumElmt : list of integer --> integer
#SumElmt(L) menghasilkan jumlah semua elemen dalam list

#2
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


#3
#LPrime(L) : list of integer --> list
#LPrime(L) menghasilkan list baru yang dimana isinya hanya bilangan prima
"""
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
"""

#4
#InsertAfter: list --> list
#InsertAfter(L,x,e) menghasilkan list baru dimana menambahkan elemen x setelah elemen e

#5
#MakeMinus: 2 set --> set
#MakeMinus(H1,H2) membuat set baru dimana anggota H1 yang BUKAN merupakan anggota H2

#6
#MakeKomplemen: 2 set --> set
#MakeKomplemen(H1,H2)   membuat set baru yang anggotanya adalah anggota semua anggota H1 dan H2
#                       tetapi bukan interseksi keduanya








    
