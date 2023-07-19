class date:
    def __init__ (self,Hr,Bln,Thn):
        self.d = Hr
        self.m = Bln
        self.y = Thn

#REALISASI SELEKTOR
def tgl(D):
    return D.d
def bln(D):
    return D.m
def thn(D):
    return D.y

#REALISASI KONSTRUKTOR
def make_date(d,m,y):
    return date(d,m,y)

#IS KABISAT
def is_kabisat(x):
    return x%4==0 and x%100!=0 or x//400==0

#DPM(b)
def dpm(b):
    if b==1:
        return 31
    elif b==2:
        return 60 
    elif b==3:
        return 91 
    elif b==4:
        return 121 
    elif b==5:
        return 152 
    elif b==6:
        return 182 
    elif b==7:
        return 213 
    elif b==8:
        return 244  
    elif b==9:
        return 274 
    elif b==10:
        return 305 
    elif b==11:
        return 335 
    elif b==12:
        return 366 

#NEXTNDAY
def nextNday(D,N):
    a=(N%365)+tgl(D)-dpm(((N%365)+tgl(D))//31)
    b=(N%365)+tgl(D)-dpm(((N%365)+tgl(D))//30)
    c=(N%365)+tgl(D)-dpm(((N%365)+tgl(D))//29)
    d=(N%365)+tgl(D)-dpm(((N%365)+tgl(D))//28)
    e=bln(D)+ ((tgl(D)+N)//31)- (12*(N//365))
    f=bln(D)+ ((tgl(D)+N)//30)- (12*(N//365)) 
    g=bln(D)+ ((tgl(D)+N)//29)
    h=bln(D)+ ((tgl(D)+N)//28)
    i=thn(D)+ ((tgl(D)+N)//366)
    j=thn(D)+ ((tgl(D)+N)//365)
    #N LEBIH DARI SETAHUN
    if tgl(D)+N > 365 and (bln(D)==1 or bln(D)== 3 or bln(D)==5 or bln(D)==7 or bln(D)==8 or bln(D)==10):
        return (a,e,j)
    elif tgl(D)+N > 365 and is_kabisat(thn(D)) and (bln(D)==1 or bln(D)== 3 or bln(D)==5 or bln(D)==7 or bln(D)==8 or bln(D)==10):
        return (a,e,i)

    elif tgl(D)+N > 365 and (bln(D)==4 or bln(D)==6 or bln(D)==9 or bln(D)==11):
        return (b,f,j)
    elif tgl(D)+N > 365 and is_kabisat(thn(D)) and (bln(D)==4 or bln(D)==6 or bln(D)==9 or bln(D)==11):
        return (b,f,i)

    

A=date(23,10,2001)
print(nextNday(A,730))

