def jadwal(h,j):
    return [h,j]

def hari(jadwal):
    return jadwal[0]
def jam(jadwal):
    return jadwal[1]

def dailymapel(jadwal):
    if(hari(jadwal)=="Senin"):
        if (jam(jadwal) == 7.00):
            return "Matematika Peminatan"
        elif (jam(jadwal) == 9.30):
            return "Fisika"
        elif (jam(jadwal) == 12.00):
            return "Kimia"
        elif (jam(jadwal) == 13.50):
            return "Biologi"
    elif(hari(jadwal)=="Selasa"):
        if (jam(jadwal) == 7.00):
            return "Olahaga"
        elif (jam(jadwal) == 9.30):
            return "Agama"
        elif (jam(jadwal) == 12.00):
            return "PKN"
        elif (jam(jadwal) == 13.50):
            return "Sejarah"
    elif (hari(jadwal)=="Rabu"):
        if (jam(jadwal) == 7.00):
            return "Seni Budaya"
        elif (jam(jadwal) == 9.30):
            return "Bahasa Indonesia"
        elif (jam(jadwal) == 12.00):
            return "Bahasa Inggris"
        elif (jam(jadwal) == 13.50):
            return "Matematika Wajib"
    else:
        return "Tidak ada jadwal"

hari1 = input()
jam1 = float(input())
jadwal1 = jadwal(hari1,jam1)
print(dailymapel(jadwal1))
