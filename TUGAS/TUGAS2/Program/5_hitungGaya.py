#Nama File  : 5_hitungGaya.py
#Deskripsi  : Menghitung gaya pada suatu benda
#Pembuat    : Abyan Ardiatama
#Tanggal    : 2 September 2022

#DEFINISI & SPESIFIKASI dari fungsi hitungGaya dengan parameter (m,a) adalah
# hitungPercepatan : 2 integer>0, integer[0..59] --> real
#   hitungPercepatan(v,t) menghitung percepatan pada sebuah benda
# 5_hitungGaya : 3 integer>0, integer>0, integer[0..59] --> real
#   hitungGaya(m,v,t) menghitung gaya dengan input yang diberikan

#REALISASI
def hitungPercepatan(v,t):
    return v / t

def hitungGaya(m,v,t):
    return m * hitungPercepatan(v,t)

#APLIKASI
print(hitungGaya(5,10,2))
print(hitungGaya(4,3,6))
print(hitungGaya(7,5,2))

