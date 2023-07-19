#Nama File  : 1_konversiDetik.py
#Deskripsi  : Mengkonversi sebuah waktu dalam satuan detik
#Pembuat    : Abyan Ardiatama
#Tanggal    : 2 September 2022

#DEFINISI & SPESIFIKASI fungsi konversiDetik dengan parameter (j,m,d)
#konversiDetik : 3 integer[0..24], integer[0..59],integer[0..59] --> integer
#   konversiDetik(j,m,d) menghitung jumlah detik pada suatu waktu

#REALISASI
def konversiDetik(j,m,d):
    return j*3600 + m*60 + d

#APLIKASI
print(konversiDetik(19,55,0))
print(konversiDetik(1,24,56))
print(konversiDetik(3,6,35))
