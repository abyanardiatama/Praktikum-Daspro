#Nama File  : UTS DASPRO NOMER 1.py
#Deskripsi  : Membuat tipe pecahan campuran beserta konstruktor dan selektornya
#Pembuat    : Abyan A.
#Tanggal    : 20 Oktober 2020

#REALISASI KONSTRUKTOR
class pc :
    def __init__(self,a,b,c):
        self.bil = a
        self.n   = b
        self.d   = c

def Makepc(bil,n,d):
    return pc(bil,n,d)

#REALISASI SELEKTOR
def bil(p):
    return p.bil
def pemb(p):
    return p.n
def peny(p):
    return p.d

#REALISASI OPERATOR TERHADAP TYPE
def PckeDesimal(p):
    return ((peny(p)*bil(p)) + pemb(p)) / peny(p)

#APLIKASI
A=pc(2,3,5)
B=pc(4,5,4)
print (PckeDesimal(A))
print (PckeDesimal(B))
