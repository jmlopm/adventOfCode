i=0

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

arr2=[[int(a),25] for a in arr]



while arr2[0][1]!=0:
    a,b=arr2.pop(0)
    if b==1:
        arr2+=calcularHijos(a,b)
        i+=1
    else:
        aux=calcularHijos(a, b)
        arr2.insert(0,aux[0])
        if len(aux)>1:
            arr2.insert(0,aux[1])
        


f.close()

print(len(arr2))