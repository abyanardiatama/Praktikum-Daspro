#Nama File      : Konversi Suhu Celcius
#Nama Pembuat   : Abyan A.
#Tanggal        : 29 September 2020
#Deskripsi      : Mengkonversi nilai besaran Celcius ke nilai besaran Reamur, Farenheit, dan Kelvin  

#DEFINISI DAN SPESIFIKASI dari fungsi Celcius_Conv bernama (temp,conv)adalah
# Celcius_Conv : real,character --> real   
#   Celcius_Conv (temp,conv) mengkonversi nilai besaran celcius ke Reamur(R), Farenheit(F), dan Kelvin(K)

#REALISASI
def Celcius_Conv(temp,conv):
    if (conv == "R"):
        return (4/5)*temp
    elif (conv == "F"):
        return (9/5)*temp+32
    elif (conv == "K"):
        return temp+273

#APLIKASI
print(Celcius_Conv(60.0,"R"))
print(Celcius_Conv(60.0,"F"))
print(Celcius_Conv(60.0,"K"))
