#Nama File : Ekspresi Boolean APAKAH VALID
#Nama Pembuat : Abyan A.
#Tanggal : 22 September 2020
#Deskripsi : Menerima sebuah besaran integer, dan menentukan apakah bilangan tersebut valid

#Definisi dan spesifikasi dari fungsi bernama Is_Valid(x) adalah:
#is_Valid : character --> boolean
#   is_Valid(x) bernilai benar jika x bernilai lebih kecil dari 7 atau lebih besar dari 725

#REALISASI
def Is_Valid(x):
    return (x<7 or x>725)

#APLIKASI
print(Is_Valid(5.5))
print(Is_Valid(456))
print(Is_Valid(-567))
print(Is_Valid(724.9))
