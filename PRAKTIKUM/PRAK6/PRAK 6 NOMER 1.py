#Nama File      : Penanggalan Versi 1
#Nama Pembuat   : Abyan A.
#Tanggal        : 29 September 2020
#Deskripsi      : Menghitung jumlah hari pada suatu tanggal(d), bulan(m), tahun(y) dari tanggal 1 bulan 1 dengan mengabaikan tahun kabisat.

#DEFINISI DAN SPESIFIKASI dari fungsi jumlah_hari bernama (d,m,y)adalah
# jumlah_hari: 3 integer>0 --> integer
#   jumlah_hari (d,m,y) menentukan jumlah hari pada suatu tanggal(d), bulan(m), dan tahun tertentu dengan mengabaikan tahun-tahun kabisat
# dpm : integer[1..12] --> integer
#   dpm(b) menentukan jumlah hari dari awal bulan(tanggal 1 bulan 1) hingga tanggal bulan berikutnya.

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
def jumlah_hari(d,m,y):
    return(dpm(m)+ d-1)

#APLIKASI
print(jumlah_hari(4,5,67))
print(jumlah_hari(23,11,101))
print(jumlah_hari(31,12,2001))
