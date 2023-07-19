#Nama File  : Pemangkatan
#Deskripsi  : Menghitung bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Pangkat : 2 integer --> integer or real
#   {Pangkat(x,y) adalah ekspresi rekursif pemangkatan untuk x pangkat y}

#REALISASI
def Pangkat(x,y):
    if y==0:
        return 1
    elif y<0:
        return 1/x**abs(y)
    else:
        return x * Pangkat(x,y-1)

#APLIKASI
print(Pangkat(2,3))
print(Pangkat(6,-3))
print(Pangkat(-4,3))
print(Pangkat(-5,-3))
