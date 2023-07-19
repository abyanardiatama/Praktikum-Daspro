class date:
    def __init__ (self,Hr,Bln,Thn):
        self.d = Hr
        self.m = Bln
        self.y = Thn

def tgl(D):
    return D.d
def bln(D):
    return D.m
def thn(D):
    return D.y

def is_kabisat(x):
    return x%4==0 and x%100!=0 or x//400==0
def nextday(D):
    a=tgl(D)
    b=bln(D)
    c=thn(D)
    d=tgl(D)+1
    e=bln(D)+1
    f=thn(D)+1
    if bln(D)==1 or bln(D)==3 or bln(D)==5 or bln(D)==7 or bln(D)==8 or bln(D)==10 and tgl(D)<31:
            return(d,b,c)
        else: return(1,e,c)

    elif bln(D)==2:
       if tgl(D)<28:
           return(d,b,c)
        else:
    return(1,e,c)
        elif tgl(D)==28 and is_kabisat(thn(D)):
            return(d,b,c)
        else:
            (1,e,c)

    elif bln(D)==4 or bln(D)==6 or bln(D)==9 or bln(D)==11:
        if tgl(D)<30:
            return(d,b,c)
        else:
            return(1,e,c)

    elif bln(D)==12:
        if tgl(D)<31:
            return(d,b,c)
        else:
            return(1,1,f)

A=date(23,11,2001)
print(nextday(A))
    
