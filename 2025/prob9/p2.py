#Paso 1 leer entrada
#Paso 2 tener array de ids
#paso 3 a la que me encuentro espacio pongo id del final 
#y vamos actualizando

def generarMapas(data):
    global lastId
    mapa={}
    espacios=[]
    espacio=False
    idActual=0
    pos=0
    for i in range(0, len(data)):
        if espacio:
            espacios.append([pos,int(data[i])])
        else:
            mapa[idActual]=[pos,int(data[i])]
            idActual+=1
            lastId+=1
        pos+=int(data[i])
        espacio=not espacio
    return mapa,espacios

def hacerEspacio(i1, i2, espacios,posis):
    espacios[i1]=[espacios[i1][0], espacios[i1][1]+espacios[i2][1]+posis]
    espacios.pop(i2)

def moverBloque(idAct, pos, mapa, indespacios,espacios):
    a,b=mapa[idAct]
    mapa[idAct]=[pos,b]
    if indespacios==len(espacios)-1:    
        espacios[indespacios][1]+=b
    else:
        hacerEspacio(indespacios,indespacios+1,espacios,b)

def cabe(datos,espacio):
    return datos[1]<=espacio[1]

def mover(ids,espacios,indIds,indEspacio):
    ids[indIds][0]=espacios[indEspacio][0]
    espacios[indEspacio][1]-=ids[indIds][1]
    espacios[indEspacio][0]+=ids[indIds][1]
    if espacios[indEspacio][1]==0:
        espacios.pop(indEspacio)
        return True
    return False

def rearrange(ids,espacios):
    for indIds in range(len(ids)-1,-1,-1):
        indEspacio=0
        ya=False
        while ids[indIds][0]>espacios[indEspacio][0] and not ya:
            if cabe(ids[indIds],espacios[indEspacio]):
                mover(ids,espacios,indIds,indEspacio)
                ya=True
            indEspacio+=1

def escribirBloque(mapa, long):
    ret=["."]*long
    for i in mapa:
        for k in range(0, mapa[i][1]):
            ret[mapa[i][0]+k]=i
    ret2=""
    for c in ret:
        ret2+=str(c)
    print(ret2)
            
def calcularSuma(ids):
    ret=0
    for i in ids:
        for k in range(0,ids[i][1]):
            ret+=i*(ids[i][0]+k)
    return ret


f=open("data")


data=f.read()
lastId=0
mapaIds,espacios=generarMapas(data)


lastId-=1

rearrange(mapaIds,espacios)

print(calcularSuma(mapaIds))



f.close()