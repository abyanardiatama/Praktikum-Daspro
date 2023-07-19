#Nama File      : Wujud Air Dalam Derajat Celcius
#Nama Pembuat   : Abyan A.
#Tanggal        : 29 September 2020
#Deskripsi      : Menentukan wujud air pada suatu tempratur(suhu) dalam celcius dan tekanan 1 atm

#DEFINISI DAN SPESIFIKASI dari fungsi Wujud_Air bernama (temp)adalah
# Wujud_Air  : real --> string   
#   Wujud_Air menentukan bagaimana wujud air pada suatu tempratur(suhu) dalam celcius dan tekanan 1 atm

#REALISASI
def Wujud_Air(temp):
    if temp<=0:
        return "Beku"
    elif temp>0 and temp<100:
        return "Cair"
    elif temp>=100:
        return "Uap"

#APLIKASI
print(Wujud_Air(126))
print(Wujud_Air(-10))
print(Wujud_Air(37))
print(Wujud_Air(99.9))
