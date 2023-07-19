# Nama File    : tipe time.py
# Deskripsi     : Membuat tipe bentukan time beserta konstruktor dan selektor-selektornya
# Pembuat      : Abyan A.
# Tanggal        : 30 September 2022

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#  type time : <h:integer[0..59],m:integer[0..59],s:integer[0..59]>
#  {<h,m,s> adalah sebuah time dengan h adalah jam, m adalah menit, dan s adalah detik}
#REALISASI
def time(h,m,s):
    return [h,m,s]

#DEFINISI DAN SPESIFIKASI SELEKTOR
#  jam : time --> integer
#  jam(T) akan mengembalikan nilai dari jam pada suatu waktu
#REALISASI
def jam(T):
    return T[0]

#  menit : time --> integer
#  menit(T) akan mengembalikan nilai dari menit pada suatu waktu
#REALISASI
def menit(T):
    return T[1]

#  detik : time --> integer
#  detik(T) akan mengembalikan nilai dari detik pada suatu waktu
#REALISASI
def detik(T):
    return T[2]

#DEFINISI DAN SPESIFIKASI OPERATOR
#  JumlahDetik : time --> integer
#  JumlahDetik(T) akan mengembalikan total detik dari suatu waktu
#REALISASI
def JumlahDetik(T):
    return jam(T)*3600 + menit(T)*60 + detik(T)

#DEFINISI DAN SPESIFIKASI PREDIKAT
#  IsBefore : 2 time --> boolean
#  IsBefore(T1,T2) akan mengembalikan nilai True jika jumlahdetik T1 < jumlahdetik T2
#REALISASI
def IsBefore(T1,T2):
    return JumlahDetik(T1) < JumlahDetik(T2)

#  IsBefore : 2 time --> boolean
#  IsBefore(T1,T2) akan mengembalikan nilai True jika jumlahdetik T1 > jumlahdetik T2
#REALISASI
def IsAfter(T1,T2):
    return JumlahDetik(T1) > JumlahDetik(T2)

#APLIKASI
t1 = time(2,56,45)
t2 = time(23,59,59)
print("Tipe Time t1 dan t2")
print(t1)
print(t2)

print("Selektor Time pada T1")
print(jam(t1))
print(menit(t1))
print(detik(t1))

print("Selektor Time pada T2")
print(jam(t2))
print(menit(t2))
print(detik(t2))

print("Jumlah Detik t1")
print(JumlahDetik(t1))

print("Jumlah Detik t2")
print(JumlahDetik(t2))

print("isBefore?(t1,t2)")
print(IsBefore(t1,t2))

print("isAfter?(t1,t2)")
print(IsAfter(t1,t2))

