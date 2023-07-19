#Nama File      : Jenis Segitiga dari Sisinya
#Nama Pembuat   : Abyan A.
#Tanggal        : 29 September 2020
#Deskripsi      : Menentukan jenis segitiga berdasarkan sisi-sisi(a,b,c) yang dimasukkan.  

#DEFINISI DAN SPESIFIKASI dari fungsi sisi bernama (a,b,c)adalah
# sisi : integer>0 --> string   
#   sisi (a,b,c) menentukan jenis apakan suatu segitiga(sama sisi, sama kaki, sembarang) berdasarkan sisi(a,b,c) yang dimasukkan

#REALISASI
def sisi (a,b,c):
    if (a==b==c):
        return "Sama Sisi"

    elif((a==b) and (b!=c)or
         (a==c) and (c!=b)or
         (b==c) and (c!=a)):
        return "Sama Kaki"

    elif (a!=b!=c):
        return "Sembarang"


#APLIKASI
print(sisi(5,6,4))
print(sisi(13,10,13))
print(sisi(4,4,4))

