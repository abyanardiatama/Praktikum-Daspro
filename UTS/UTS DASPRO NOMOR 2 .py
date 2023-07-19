def tanggal(nik):
    return (int(nik[6:8]))

def bulan(nik):
    return (int(nik[8:10]))

def tahun (nik):
    return (int(nik[10:12]))

def makedate(nik,jk):
    if jk=='perempuan':
        if tahun(nik)>40:
            if bulan(nik)==1:
                return (tanggal(nik)-40,'Januari',1900+tahun(nik))
            elif bulan(nik)==2:
               return (tanggal(nik)-40,'Februari',1900+tahun(nik))
            elif bulan(nik)==3:
                return (tanggal(nik)-40,'Maret',1900+tahun(nik))
            elif bulan(nik)==4:
                return (tanggal(nik)-40,'April',1900+tahun(nik))
            elif bulan(nik)==5:
                return (tanggal(nik)-40,'Mei',1900+tahun(nik))
            elif bulan(nik)==6:
                return (tanggal(nik)-40,'Juni',1900+tahun(nik))
            elif bulan(nik)==7:
                return (tanggal(nik)-40,'Juli',1900+tahun(nik))
            elif bulan(nik)==8:
                return (tanggal(nik)-40,'Agustus',1900+tahun(nik))
            elif bulan(nik)==9:
                return (tanggal(nik)-40,'September',1900+tahun(nik))
            elif bulan(nik)==10:
                return (tanggal(nik)-40,'Oktober',1900+tahun(nik))
            elif bulan(nik)==11:
                return (tanggal(nik)-40,'November',1900+tahun(nik))
            elif bulan(nik)==12:
                return (tanggal(nik)-40,'Desember',1900+tahun(nik))
        elif tahun(nik) < 40:
            if bulan(nik)==1:
                return (tanggal(nik)-40,'Januari',2000+tahun(nik))
            elif bulan(nik)==2:
               return (tanggal(nik)-40,'Februari',2000+tahun(nik))
            elif bulan(nik)==3:
                return (tanggal(nik)-40,'Maret',2000+tahun(nik))
            elif bulan(nik)==4:
                return (tanggal(nik)-40,'April',2000+tahun(nik))
            elif bulan(nik)==5:
                return (tanggal(nik)-40,'Mei',2000+tahun(nik))
            elif bulan(nik)==6:
                return (tanggal(nik)-40,'Juni',2000+tahun(nik))
            elif bulan(nik)==7:
                return (tanggal(nik)-40,'Juli',2000+tahun(nik))
            elif bulan(nik)==8:
                return (tanggal(nik)-40,'Agustus',2000+tahun(nik))
            elif bulan(nik)==9:
                return (tanggal(nik)-40,'September',2000+tahun(nik))
            elif bulan(nik)==10:
                return (tanggal(nik)-40,'Oktober',2000+tahun(nik))
            elif bulan(nik)==11:
                return (tanggal(nik)-40,'November',2000+tahun(nik))
            elif bulan(nik)==12:
                return (tanggal(nik)-40,'Desember',2000+tahun(nik))
    elif jk=='laki laki':
         if tahun(nik) > 40:    
            if bulan(nik)==1:
                return (tanggal(nik),'Januari',1900+tahun(nik))
            elif bulan(nik)==2:
               return (tanggal(nik),'Februari',1900+tahun(nik))
            elif bulan(nik)==3:
                return (tanggal(nik),'Maret',1900+tahun(nik))
            elif bulan(nik)==4:
                return (tanggal(nik),'April',1900+tahun(nik))
            elif bulan(nik)==5:
                return (tanggal(nik),'Mei',1900+tahun(nik))
            elif bulan(nik)==6:
                return (tanggal(nik),'Juni',1900+tahun(nik))
            elif bulan(nik)==7:
                return (tanggal(nik),'Juli',1900+tahun(nik))
            elif bulan(nik)==8:
                return (tanggal(nik),'Agustus',1900+tahun(nik))
            elif bulan(nik)==9:
                return (tanggal(nik),'September',1900+tahun(nik))
            elif bulan(nik)==10:
                return (tanggal(nik),'Oktober',1900+tahun(nik))
            elif bulan(nik)==11:
                return (tanggal(nik),'November',1900+tahun(nik))
            elif bulan(nik)==12:
                return (tanggal(nik),'Desember',1900+tahun(nik))
         elif tahun(nik) < 40:
            if bulan(nik)==1:
                return (tanggal(nik),'Januari',2000+tahun(nik))
            elif bulan(nik)==2:
               return (tanggal(nik),'Februari',2000+tahun(nik))
            elif bulan(nik)==3:
                return (tanggal(nik),'Maret',2000+tahun(nik))
            elif bulan(nik)==4:
                return (tanggal(nik),'April',2000+tahun(nik))
            elif bulan(nik)==5:
                return (tanggal(nik),'Mei',2000+tahun(nik))
            elif bulan(nik)==6:
                return (tanggal(nik),'Juni',2000+tahun(nik))
            elif bulan(nik)==7:
                return (tanggal(nik),'Juli',2000+tahun(nik))
            elif bulan(nik)==8:
                return (tanggal(nik),'Agustus',2000+tahun(nik))
            elif bulan(nik)==9:
                return (tanggal(nik),'September',2000+tahun(nik))
            elif bulan(nik)==10:
                return (tanggal(nik),'Oktober',2000+tahun(nik))
            elif bulan(nik)==11:
                return (tanggal(nik),'November',2000+tahun(nik))
            elif bulan(nik)==12:
                return (tanggal(nik),'Desember',2000+tahun(nik))


print (makedate('3374026011980003','perempuan'))
print (makedate('3374022311010003','laki laki'))
