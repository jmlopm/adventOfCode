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

f=open(path+"dataex")

tablero=[]

for l in f:
    tablero.append(l.replace("\n",''))

ret=0
for i in range(0,len(tablero)):
    for j in range(0,len(tablero[i])):
        if tablero[i][j]=="@":
            ret+=int(nadyacentes(i,j,tablero)<4)
print(ret)
f.close()