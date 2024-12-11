i=0

mapa={}

def iterar(mapa):
    mapa2={}
    mapa2[1]=0
    for m in mapa:
        mapa2[m]=0
    for m in mapa:
        if m==0:
            mapa2[1]+=mapa[m]
        elif len(str(m))%2==0:
            a,b=int(str(m)[0:len(str(m))//2]),int(str(m)[len(str(m))//2:len(str(m))])
            if a in mapa2:
                mapa2[a]+=mapa[m]
            else:
                mapa2[a]=mapa[m]
                
            if b in mapa2:
                mapa2[b]+=mapa[m]
            else:
                mapa2[b]=mapa[m]
        else:
            aux=m*2024
            if aux in mapa2:
                mapa2[aux]+=mapa[m]
            else:
                mapa2[aux]=mapa[m]
    return mapa2
        

def calcularHijos(elem, its):
    global i
    if its==0:
        return [[elem,0]]
    else:
        if elem==0:
            return [[1,its-1]]
        if len(str(elem))%2==0:
            a,b=str(elem)[0:len(str(elem))//2],str(elem)[len(str(elem))//2:len(str(elem))]
            return[[int(a),its-1],[int(b),its-1]]
        return [[2024*elem,its-1]]
    
f=open("data")

arr=f.readline().replace("\n","").split(" ")

ret=0

for e in arr:
    mapa[int(e)]=1
    
for i in range(0,75):
    mapa=iterar(mapa)
    
    
arr2=[[int(a),5] for a in arr]



f.close()

print(len(mapa))

ret=0
for k in mapa:
    ret+=mapa[k]
print(ret)
