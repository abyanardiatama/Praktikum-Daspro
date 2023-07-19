#Nama File      : Penanggalan Versi 2
#Nama Pembuat   : Abyan A.
#Tanggal        : 29 September 2020
#Deskripsi      : Menghitung jumlah hari pada suatu tanggal(d), bulan(m), tahun(y) dari tanggal 1 bulan 1 dengan memperhitungkan tahun kabisat

#DEFINISI DAN SPESIFIKASI dari fungsi MO bernama (u,v,w,x)adalah
# jumlah_hari_kabisat : 3 integer>0 --> integer
#   jumlah_hari_kabisat (d,m,y) menentukan maksimum dari 4 buah bilangan integer
# dpm : integer>0 --> integer
#   dpm(b) menyatakan jumlah hari suatu bulan dihitung dari tanggal 1 bulan 1 hingga tanggal 1 bulan berikutnya
# is_kabisat : integer --> boolean
#   is_kabisat menentukan apakah tahun yang dimasukkan merupakan tahun kabisat

#REALISASI
def dpm(b):
    if b==1:
        return 1
    elif b==2:
        return 32
    elif b==3:
        return 60
    elif b==4:
        return 91
    elif b==5:
        return 121
    elif b==6:
        return 152
    elif b==7:
        return 182
    elif b==8:
        return 213
    elif b==9:
        return 244
    elif b==10:
        return 274
    elif b==11:
        return 305
    elif b==12:
        return 335
def is_kabisat(x):
    return  (x%4 == 0) and (x%100 != 0) or (x//400 == 0)  
def jumlah_hari_kabisat(d,m,y):
    return dpm(m)+ d-1+ 1 if m>2 and is_kabisat(y) else dpm(m)+d-1+0

#APLIKASI
print(jumlah_hari_kabisat(1,10,1964))
print(jumlah_hari_kabisat(23,11,1924))
print(jumlah_hari_kabisat(11,4,2001))
print(is_kabisat(1924))
