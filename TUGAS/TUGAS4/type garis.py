# Nama File    : garis.py
# Deskripsi     : Membuat tipe bentukan garis beserta konstruktor dan selektornya
# Pembuat      : Abyan Ardiatama
# Tanggal       : 30 September 2022

import math
#DEFINISI TYPE
#  type garis : <P1 : point, P2 : point>
#  {<P1,P2> adalah sebuah garis yang melalui 2 titik, dengan P1 adalah titik1 dan P2 adalah titik2 }

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#  point : 2 integer --> point
#  point(x,y) membentuk sebuah point dengan x adalah absis dan y adalah ordinat
#  REALISASI
def point(x,y):
    return [x,y]

#  garis : 2 point --> garis
#  garis(P1,P2) membentuk sebuah garis dengan P1 adalah Titik1 dan P2 adalah Titik2
#  REALISASI
def garis(P1, P2 ):
    return [P1, P2]

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#  absis : point --> integer
#  absis(P) mengembalikan nilai x pada point
#  REALISASI
def absis(P):
    return P[0]

#  ordinat : point --> integer
#  ordinat(P) mengembalikan nilai y pada point
def ordinat(P):
    return P[1]

#  Titik1 : garis --> point
#  Titik1(G) mengembalikan nilai P1 sebagai titik awal
#REALISASI
def Titik1(G):
    return G[0]

#  Titik2 : garis --> point
#  Titik2(G) mengembalikan nilai P2 sebagai titik awal
#REALISASI
def Titik2(G):
    return G[1]

#DEFINISI DAN SPESIFIKASI OPERATOR
#  Gradien : garis --> integer
#  Gradien(G) mengembalikan nilai gradien pada suatu garis G
#  REALISASI
def Gradien(G):
    y = ordinat(Titik2(G))-ordinat(Titik1(G))
    x = absis(Titik2(G)) - absis(Titik1(G))
    return y / x

#  PanjangGaris : garis --> integer
#  PanjangGaris(G) mengembalikan nilai panjang garis pada suatu garis G
#  REALISASI
def PanjangGaris(G):
    x = (absis(Titik2(G)) - absis(Titik1(G)))**2
    y = (ordinat(Titik2(G)) - ordinat(Titik1(G)))**2
    return math.sqrt(x+y)

#  TitikPotongX : garis --> point
#  TitikPotongX(G) mengembalikan titik perpotongan pada sumbu X
#  REALISASI
def TitikPotongX(G):
    x = absis(Titik2(G)) - absis(Titik1(G))
    y = ordinat(Titik2(G)) - ordinat(Titik1(G))
    TipotX = (-ordinat(Titik1(G)) + (Gradien(G)*absis(Titik1(G))))/Gradien(G)
    #TipotX = (-ordinat(P1)*x + absis(P1)*y) / y
    return (TipotX,0)

#  TitikPotongY : garis --> point
#  TitikPotongY(G) mengembalikan titik perpotongan pada sumbu Y
#  REALISASI
def TitikPotongY(G):
    x = absis(Titik2(G)) - absis(Titik1(G))
    y = ordinat(Titik2(G)) - ordinat(Titik1(G))
    TipotY = (-absis(Titik1(G))*y + ordinat(Titik1(G))*x) / x
    return 0,TipotY

#  DEFINISI DAN SPESIFIKASI PREDIKAT
#  IsSejajar(G1,G2) : 2 garis --> boolean
#  IsSejajar(G1,G2) mengembalikan nilai true jika gradien G1 = G2
#  REALISASI
def isSejajar(G1,G2):
    return Gradien(G1) == Gradien(G2)

#  IsTegakLurus(G1,G2) : 2 garis --> boolean
#  IsTegakLurus(G1,G2) mengembalikan nilai true jika gradien G1* G2=-1
#  REALISASI
def isTegakLurus(G1,G2):
    return Gradien(G1)*Gradien(G2) == -1

#APLIKASI
t1 = point(2,3)
t2 = point(3,6)
t3 = point(3,4)
t4 = point(6,8)
t5 = point(1,2)
t6 = point(3,7)

g1 = garis(t1,t2)
g2 = garis(t5,t6)
print("Garis G dan G2")
print(garis(t1,t2))
print(garis(t5,t6))
print("Selektor garis G")
print(Titik1(g1))
print(Titik2(g1))
print("Selektor garis G2")
print(Titik1(g2))
print(Titik2(g2))
print("Gradien G dan G2")
print(Gradien(g1))
print(Gradien(g2))
print("Panjang Garis G")
print(PanjangGaris(g1))
print(PanjangGaris(g2))
print("Titik Potong X dan Y garis G")
print(TitikPotongX(g1))
print(TitikPotongY(g1))
print("Titik Potong X dan Y garis G2")
print(TitikPotongX(g2))
print(TitikPotongY(g2))
print("IsSejajar?(g1,g2)")
print(isSejajar(g1,g2))
print("IsTegakLurus?(g1,g2)")
print(isTegakLurus(g1,g2))

