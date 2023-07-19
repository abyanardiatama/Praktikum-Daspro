#Nama File  : 4_isKabisat.py
#Deskripsi  : Mengecek apakah sebuah tahun merupakan tahun kabisat
#Pembuat    : Abyan Ardiatama
#Tanggal    : 2 September 2022

#DEFINISI & SPESIFIKASI dari fungsi isKabisat dengan parameter thn adalah
#isKabisat : 1 integer>0 --> boolean

#REALISASI
def isKabisat(thn):
    if(thn%400==0 or (thn%4==0 and thn%100>0)):
        print("Tahun %d adalah tahun kabisat" % thn)
    else:
        print("Tahun %d bukan tahun kabisat" % thn)

#APLIKASI
isKabisat(2000)
isKabisat(1996)
isKabisat(1998)
