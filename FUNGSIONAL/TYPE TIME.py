#Nama File  : type time.py
#Deskripsi  : Membuat tipe time beserta konstruktor dan selektornya
#Pembuat    : Abyan A.  
#Tanggal    : 9 Oktober 2020 

#DEFINISI TYPE
# type time : < j:integer[0...23],m:integer[0...59],d:integer[0...59] >
#   {j:integer[0...23],m:integer[0...59],d:integer[0...59] adalah jam, meni, detik pada suatu time}

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makeTime : integer[0...23],integer[0...59],integer[0...59] --> time
#   {makeTime(x,y,z) membentuk time dengan jam x, menit y, dan detik z}

#DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
# jam : time --> integer[0...23]
#   {jam(D)menentukan nilai jam dari sebuah time}
# menit : time --> integer[0..59]
#   {menit(D)menentukan nilai menit dari sebuah time}
# detik : time --> integer[0...59]
#   {detik(D) menentukan nilai detik dari sebuah time}

#DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP TIME
# KonversiDetikToTime : integer>0 --> time
#   {KonversiDetikToTime(x) mengkonversi detik x menjadi sebuah time}
# JumlahDetik : time --> detik
#   {JumlahDetik(T) menghitung jumlah detik dari sebuah time}
# AddTime : 2 time --> time
#   {AddTime(T1,T2) menjumlahkan 2 buah time menghasilkan sebuah time}
# AddTimeDetik : time, integer>0 --> time
#   {AddTimeDetik(T,N) menjumlahkan sebuah time dengan detik N menghasilkan sebuah time}
#DEFINISI DAN SPESIFIKASI PREDIKAT
# isBefore : 2 time --> boolean
#   {isBefore(T1,T2) bernilai benar jika T1 adalah sebelum T2}
# isAfter : 2 time --> boolean
#   {isAfter(T1,T2) bernilai benar jika T1 adalah setelah T2}

################################################################################################################
#REALISASI TYPE
class time:
    def __init__(self,a,b,c):
        self.j = a
        self.m = b
        self.d = c

#REAKISASI KONSTRUKTOR
def makeTime(j,m,d):
    return (j,m,d)

#REALISASI SELEKTOR
def jam(t):
    return t.j
def menit(t):
    return t.m
def detik(t):
    return t.d

#REALISASI OPERATOR TERHADAP TIME
def KonversiDetikToTime(N):
    a= 0 if N//3600 >= 24 else N//3600
    b= (N % 3600) // 60
    c=((N % 3600) % 60)
    return(a,b,c)

def jumlahdetik(T):
    return jam(T)*3600 + menit(T)*60 + detik(T)

def AddTime(t1,t2):
    return KonversiDetikToTime(jumlahdetik(t1)+jumlahdetik(t2))

def AddTimeDetik(T,N):
    return KonversiDetikToTime(jumlahdetik(T)+ N)

#REALISASI PREDIKAT
def isBefore(T1,T2):
    return(jumlahdetik(T1) < jumlahdetik(T2))

def isAfter(T1,T2):
    return(jumlahdetik(T1) > jumlahdetik(T2))

################################################################################################################
#APLIKASI TYPE
A=time(23,11,30)
B=time(9,11,40)

#APLIKASI SELRKTOR DAN KONSTRUKTOR
print (jam(A))
print (menit(B))
print (menit(B))
print (makeTime(23,59,59))

#APLIKASI OPERATOR TERHADAP TYPE
print(KonversiDetikToTime(86500))
print(KonversiDetikToTime(4000))
print(jumlahdetik(A))
print(jumlahdetik(B))
print(AddTime(A,B))
print(AddTimeDetik(A,4000))


#APLIKASI PREDIKAT
print(isBefore(A,B))
print(isAfter(A,B))
