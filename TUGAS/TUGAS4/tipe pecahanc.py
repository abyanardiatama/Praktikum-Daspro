# Nama File    : pecahanC.py
# Deskripsi     : Membuat tipe bentukan pecahan campuran beserta konstruktor dan selektornya
# Pembuat      : Abyan Ardiatama
# Tanggal       : 30 September 2022

#DEFINISI TYPE
#  type pecahanC : <bil:integer,n:integer>=0,d:integer>0>
#  {<bil,n,d> adalah sebuah pecahan campuran, dengan bil adalah bilangan, n adalah pembilang, dan d adalah penyebut }

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#  pecahanC : 3 integer --> pecahanC
#  pecahanC(bil,n,d) membentuk sebuah pecahan campuran dari bil adalah bilangan, n adalah pembilang, dan d adalah penyebut 
#  REALISASI
def pecahanC(bil,n,d):
    return [bil,n,d]

#DEFINISI DAN SPESIFIKASI SELEKTOR
#  bil : pecahanC --> integer
#  bil(P) memberikan bilangan pada pecahan campuran
#REALISASI
def bil(P):
    return P[0]

#  num : pecahanC --> integer
#  num(P) memberikan pembilang pada pecahan campuran
#REALISASI
def num(P):
    return P[1]

#  denum : pecahanC --> integer
#  denum(P) memberikan penyebut pada pecahan campuran
#REALISASI
def denum(P):
    return P[2]

#DEFINISI DAN SPESIFIKASI OPERATOR
#  KonversiPecahan : pecahanC --> 2 integer
#  KonversiPecahan(P) mengkonversi pecahan campuran menjadi pecahan biasa
#REALISASI
def KonversiPecahan(P):
    return P[0] * P[2] + P[1] , P[2]

#  KonversiReal : pecahanC --> real
#  KonversiReal(P) mengkonversi pecahan campuran menjadi bilangan real
#REALISASI
def KonversiReal(P):
    return (P[0]*P[2]+P[1]) / P[2]

#  AddP : 2 pecahanC --> 2 integer
#  AddP(P1,P2) mengembalikan hasil dari penjumlahan 2 pecahan campuran
#REALISASI
def AddP(P1,P2):
    pemb1 = bil(P1)*denum(P1)+num(P1)
    pemb2 = bil(P2)*denum(P2)+num(P2)
    x = (pemb1*denum(P2)) + (pemb2*denum(P1))
    y = denum(P1)*denum(P2)
    return x,y

#  SubP : 2 pecahanC --> 2 integer
#  SubP(P1,P2) mengembalikan hasil dari pengurangan 2 pecahan campuran
#REALISASI
def SubP(P1,P2):
    pemb1 = bil(P1)*denum(P1)+num(P1)
    pemb2 = bil(P2)*denum(P2)+num(P2)
    x = (pemb1*denum(P2)) - (pemb2*denum(P1))
    y = denum(P1)*denum(P2)
    return x,y

#  DivP : 2 pecahanC --> 2 integer
#  DivP(P1,P2) mengembalikan hasil dari pembagian 2 pecahan campuran
#REALISASI
def DivP(P1,P2):
    pemb1 = bil(P1)*denum(P1)+num(P1)
    pemb2 = bil(P2)*denum(P2)+num(P2)
    x = pemb1 * denum(P2)
    y = denum(P1) * pemb2
    return x,y

#  MulP : 2 pecahanC --> 2 integer
#  MulP(P1,P2) mengembalikan hasil dari perkalian 2 pecahan campuran
#REALISASI
def MulP(P1,P2):
    pemb1 = bil(P1)*denum(P1)+num(P1)
    pemb2 = bil(P2)*denum(P2)+num(P2)
    x = pemb1 * pemb2
    y = denum(P1) * denum(P2)
    return x,y

#DEFINISI DAN SPESIFIKASI PREDIKAT
#  IsEqP? : 2 pecahanC --> boolean
#  IsEqP?(P1,P2) mengembalikan nilai true jika P1 sama dengan P2
#REALISASI
def IsEqP(P1,P2):
    pemb1 = bil(P1)*denum(P1)+num(P1)
    pemb2 = bil(P2)*denum(P2)+num(P2)
    return pemb1 * denum(P2) == pemb2*denum(P1)

#  IsLtP? : 2 pecahanC --> boolean
#  IsLtP?(P1,P2) mengembalikan nilai true jika P1 kurang dari P2
#REALISASI
def IsLtP(P1,P2):
    pemb1 = bil(P1)*denum(P1)+num(P1)
    pemb2 = bil(P2)*denum(P2)+num(P2)
    return pemb1 * denum(P2) < pemb2*denum(P1)

#  IsGtP? : 2 pecahanC --> boolean
#  IsGtP?(P1,P2) mengembalikan nilai true jika P1 lebih dari P2
#REALISASI
def IsGtP(P1,P2):
    pemb1 = bil(P1)*denum(P1)+num(P1)
    pemb2 = bil(P2)*denum(P2)+num(P2)
    return pemb1 * denum(P2) > pemb2*denum(P1)

#APLIKASI
P1 = pecahanC(2,3,4)
P2 = pecahanC(3,4,5)
print(P1)
print(bil(P1))
print(num(P1))
print(denum(P1))
print(KonversiPecahan(P1))
print(KonversiReal(P1))
print(AddP(P1,P2))
print(SubP(P1,P2))
print(DivP(P1,P2))
print(MulP(P1,P2))
print(IsEqP(P1,P2))
print(IsGtP(P1,P2))
print(IsLtP(P1,P2))
