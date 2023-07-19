#Nama File : GanjilGenap.py
#Nama Pembuat : Abyan Ardiatama
#Tanggal : 15 September 2022
#Deskripsi : Menentukan apakah input merupakan bilangan ganjil atau genap

#Definisi dan spesifikasi dari fungsi GanjilGenap
# GanjilGenap : integer --> string

#REALISASI
def GanjilGenap(x):
    if(x%2==0):
        return "Genap"
    else:
        return "Ganjil"

#APLIKASI
print(GanjilGenap(2))
print(GanjilGenap(5))
print(GanjilGenap(7))
