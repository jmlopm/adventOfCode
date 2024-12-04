import numpy as np

def comprobarFilaAdelante(i,j,dat):
    if j<len(dat)-3:
        return dat[i][j:j+4]=="XMAS"
    return False
    
def comprobarFilaAtras(i,j,dat):
    if j>2:
        return dat[i][j-3:j+1][::-1]=="XMAS"
    return False
def comprobarColumnaAdelante(i,j,dat):
    if i<len(dat[0])-3:
        return ''.join(dat[i][j]+dat[i+1][j]+dat[i+2][j]+dat[i+3][j])=="XMAS"
    return False
def comprobarColumnaAtras(i,j,dat):
    if i>2:
        return ''.join(dat[i-3][j]+dat[i-2][j]+dat[i-1][j]+dat[i][j])=="SAMX"
    return False
def comprobarDiagonalAdelante(i,j,dat):
    if i<len(dat)-3 and j<len(dat)-3:
        aux=[dat[i+k][j+k] for k in range(0,4)]
        return ''.join(aux)=="XMAS"
    return False
def comprobarDiagonalAdelante2(i,j,dat):
    if i<len(dat)-3 and j>2:
        aux=[dat[i+k][j-k] for k in range(0,4)]
        return ''.join(aux)=="XMAS"
    return False
def comprobarDiagonalAtras(i,j,dat):
    if i>2 and j>2:
        aux=[dat[i-k][j-k] for k in range(0,4)]
        return ''.join(aux)=="XMAS"
    return False
def comprobarDiagonalAtras2(i,j,dat):
    if i>2 and j<len(dat)-3:
        aux=[dat[i-k][j+k] for k in range(0,4)]
        return ''.join(aux)=="XMAS"
    return False

f=open("data")
dat=[]
for l in f:
    dat.append(l[0:len(l)-1])
#datTrans=np.transpose(dat)

cont=0
for i in range(0,len(dat)):
    for j in range(0,len(dat[0])):
        if dat[i][j]=='X':
            if comprobarFilaAdelante(i, j, dat):
                cont+=1
            if comprobarFilaAtras(i, j, dat):
                cont+=1
            if comprobarColumnaAdelante(i, j, dat):
                cont+=1
            if comprobarColumnaAtras(i, j, dat):
                cont+=1
            if comprobarDiagonalAdelante(i, j, dat):
                cont+=1
            if comprobarDiagonalAtras(i, j, dat):
                cont+=1
            if comprobarDiagonalAtras2(i, j, dat):
                cont+=1
            if comprobarDiagonalAdelante2(i, j, dat):
                cont+=1
print(cont)