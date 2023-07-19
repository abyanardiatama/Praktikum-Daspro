#Nama File      : Hasil Pembagian 2 Akar 
#Nama Pembuat   : Abyan A.
#Tanggal        : 29 September 2020
#Deskripsi      : Menghitung hasil bagi dari 2 akar dari nilai-nilai yang dimasukkan

#Definisi dan spesifikasi dari fungsi hasil_bagi bernama(a,b,c)adalah
# hasil_bagi : 3 integer --> real
#   hasil_bagi(a,b,c) menghitung pembagian dari 2 akar yang dihitung sebelumnya
# Akar1 : 3 integer --> real
#   Akar1(x,y,z) menghitung nilai akar dari rumus yang telah ditentukan
# Akar2 : 3 integer --> real
#   Akar2(p,q,r) menghitung nilai akar dari rumus yang telah ditentukan
# disk : 3 integer --> real
#   disk(j,k,l) menhitung nilai diskriminan, dan disk>0

#REALISASI
import math
def disk(j,k,l):
    return math.sqrt(k**2-4*j*l)
def Akar1(x,y,z):
    return ((-y+disk(x,y,z))/(2*x))
def Akar2(p,q,r):
    return ((-q-disk(p,q,r))/(2*p))

def hasil_bagi(a,b,c):
    if Akar1(a,b,c) > Akar2(a,b,c):
        return Akar1(a,b,c)/Akar2(a,b,c)
    elif Akar1(a,b,c) < Akar2(a,b,c):
        return Akar2(a,b,c)/Akar1(a,b,c)


#APLIKASI
print(hasil_bagi(2,-10,8))
print(hasil_bagi(1,1,-2))
print(hasil_bagi(3,-10,3))
print(Akar2(1,-5,4))

