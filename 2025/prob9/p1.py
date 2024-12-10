#Paso 1 leer entrada
#Paso 2 tener array de ids
#paso 3 a la que me encuentro espacio pongo id del final 
#y vamos actualizando

def generarArray(data):
    ret=[]
    espacio=False
    idActual=0
    for i in range(0, len(data)):
        if espacio:
            ret+=[-1]*int(data[i])
        else:
            ret+=[idActual]*int(data[i])
            idActual+=1
        espacio=not espacio
    return ret

def rearrange(arr):
    final=len(arr)-1
    ret=[]
    i=0
    while i<final:
        if arr[i]!=-1:
            ret+=[arr[i]]
        else:
            while arr[final]==-1 and i<final:
                final-=1
            ret+=[arr[final]]
            final-=1
        i+=1
    print(i,final)
    return ret
            
def calcularSuma(arr):
    ret=0
    for i in range(0,len(arr)):
        if arr[i]==-1:
            return ret
        ret+=i*int(arr[i])
    return ret


f=open("data")

data=f.read()

arr1=generarArray(data)

arr2=rearrange(arr1)

print(calcularSuma(arr2))



f.close()