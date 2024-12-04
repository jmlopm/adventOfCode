import numpy as np

def comprobarCaja(i,j,dat):
    d1=''.join([dat[i-1+k][j-1+k] for k in range(0,3)])
    d2=''.join([dat[i+1-k][j-1+k] for k in range(0,3)])
    return (d1=="MAS" or d1 =="SAM") and (d2=="MAS" or d2=="SAM")
f=open("data")
dat=[]
for l in f:
    dat.append(l[0:len(l)-1])
#datTrans=np.transpose(dat)

cont=0
for i in range(1,len(dat)-1):
    for j in range(1,len(dat[0])-1):
        if dat[i][j]=='A':
            if comprobarCaja(i, j, dat):
                cont+=1
print(cont)