import ast
def jmlElmt(S):
    if(S==[]):
        return 0
    else:
        return S[0]+jmlElmt(S[1:])
S=[[1,2,3],4]
print(jmlElmt(S[0]))
def penjual_permen(L):
    if(L==[]):
        return 0
    else:
        if(type(L[0])==list):
            if(jmlElmt(L[0])%2 == 0):
                return (jmlElmt(L[0])*2000)+penjual_permen(L[1:])
            else:
                return (jmlElmt(L[0])*1000)+penjual_permen(L[1:])
        else:
            if(L[0]%2==0):
                return (L[0]*4000) + penjual_permen(L[1:])
            else:
                return (L[0]*3000) + penjual_permen(L[1:])
L=ast.literal_eval(input())
print(penjual_permen(L))
