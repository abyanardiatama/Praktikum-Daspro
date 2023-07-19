#Nama File  : Ekspresi Rekursif
#Deskripsi  : Menghitung bilangan dengan operasi reksursif
#Pembuat    : Abyan A.
#Tanggal    : 26 Oktober 2020

#DEFINISI SPESIFIKASI
#Kuadrat : integer>0 --> integer
#   {Kuadrat(n) menghitung jumlah deret dari n pangkat 2}

#REALISASI
#NO9
def Kuadrat(n):
    if n==0:
        return 0
    else:
        return n**2 + (Kuadrat(n-1))

#APLIKASI
print(Kuadrat(5))
print(Kuadrat(8))
print(Kuadrat(10))
print(Kuadrat(15))
