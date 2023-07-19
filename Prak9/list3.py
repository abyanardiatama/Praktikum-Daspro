#Nama		: 
#NIM		: 
#Tanggal	: 
#Deskripsi	: 

from list2 import *

list1 = [1, [2], 3, 4, [5,6]]

list2 = [1, [1,2,3], 3, 4, [4,5,6]]

Matrix1 =	[
				[1,2,3],
				[4,5,6],
				[7,8,9]
			]
		
Matrix2 =[[1,0,0],[0,1,0],[0,0,1]]
		

#DefSpek
#IsAtom : list --> boolean
#IsAtom(e) bernilai benar jika elemen list adalah sebuah atom

def IsAtom(e):
	if(type(e) != list):
		return True
	else:
		return False

#DefSpek
#IsList : list --> boolean
#IsList(e) bernilai benar jika element list adalah sebuah list

def IsList(e):
	if(type(e) == list):
		return True
	else:
		return False


#DefSpek
#Jumlah : list --> integer
#Jumlah (L) menghasilkan jumlah seluruh elemen dalam list

def Jumlah(L):
	if(IsEmpty(L)):
		return 0
	elif(IsList(FirstElmt(L))):
		return Jumlah(FirstElmt(L)) + Jumlah(Tail(L))
	else:	
		return FirstElmt(L) + Jumlah(Tail(L))
        
def NilaiTengah(L):
    return L[len(L)//2]

def Concat(L1, L2):
	return L1+L2