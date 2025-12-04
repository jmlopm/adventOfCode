path="C:/Users/josem/Desktop/AoC/2026/prob4/"

def nadyacentes(i,j,tablero):
    ret=0
    for a in range(-1,2):
        for b in range(-1,2):
            if a!=0 or b!=0:
                if i+a>=0 and j+b>=0 and i+a<len(tablero) and j+b<len(tablero[0]):
                    if tablero[i+a][j+b]=="@":
                        ret+=1    
    return ret

f=open(path+"data")

tablero=[]

for l in f:
    aux=[]
    for c in l:
        if c!="\n":
            aux.append(c)
    tablero.append(aux)

ret=0
hayCambio=True
while hayCambio:
    hayCambio=False
    for i in range(0,len(tablero)):
        for j in range(0,len(tablero[i])):
            if tablero[i][j]=="@":
                if nadyacentes(i,j,tablero)<4:
                    ret+=1
                    tablero[i][j]="."
                    hayCambio=True
print(ret)
f.close()