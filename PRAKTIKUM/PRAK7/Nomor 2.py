# Nama File : Nomor 2.py
# Pembuat   : Alfrethanov Christian Wijaya
# Tanggal   : Kamis, 8 Oktober 2020
# Deskripsi : Didefinisikan suatu type Date yang terdiri dari hari, bulan, dan tahun dan membentuk komposisi <Hr, Bln, Thn>.

# Definisi dan Spesifikasi TYPE
# type Absis : real
# {definisi ini hanyalah untuk "menanamkan" type integer dengan nilai tertentu untuk mewakili absis suatu titik.}

# type Oordinat : real
# {definisi ini hanyalah untuk "menanamkan" type integer dengan nilai tertentu untuk mewakili oordinat suatu titik.}

# type Point : <x: Nilai x suatu titik (absis), y: Nilai y suatu titik (oordinat)>
# {<x,y> adalah titik dengan absis x dan oordinat y.}

# Definisi dan Spesifikasi SELEKTOR
# xP : Point -> Absis
# {xP(P) memberikan absis x dari P yang terdiri dari <x,y>.}

# yP : Point -> Oordinat
# {yP(P) memberikan oordinat y dari P yang terdiri dari <x,y>.}

# Definisi dan Spesifikasi KONSTRUKTOR
# MakeLine : <Absis,Oordinat> -> Point
# {MakeLine<(x,y)> -> Titik pada absis dan oordinat yang bersangkutan.}

# Definisi dan Spesifikasi OPERATOR/FUNGSI lain terhadap Date
# Gradien : 2 Point -> real
# {Gradien(P1,P2) : menghitung nilai gradien dari sebuah garis yang melalui 2 titik tertentu.}

# Definisi dan Spesifikasi Predikat
# IsSejajar : 4 Point -> boolean
# {IsSejajar(L1,L2,L3,L4) : menentukan apakah garis 1 dan 2 yang masing-masing melalui 2 titik tertentu saling sejajar. Hasil akan True apabila kedua garis Sejajar.}

# IsTegakLurus : 4 Point -> boolean
# {IsTegakLurus(L1,L2,L3,L4) : menentukan apakah garis 1 dan 2 yang masing-masing melalui 2 titik tertentu saling tegak lurus. Hasil akan True apabila kedua garis Tegak Lurus.}

#Realisasi

class Point:
    def __init__(self,p,q):
        self.x = p
        self.y = q

def xP(P):
    return P.x

def yP(P):
    return P.y

def MakeLine(x,y):
    return Point(x,y)

def Gradien(P1,P2):
    return (yP(P2)-yP(P1))/(xP(P2)-xP(P1))

def IsSejajar(L1,L2,L3,L4):
    return Gradien(L1,L2) == Gradien(L3,L4)

def IsTegakLurus(L1,L2,L3,L4):
    return Gradien(L1,L2) * Gradien(L3,L4) == -1
