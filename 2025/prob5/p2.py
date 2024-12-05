def encontrarMin(l):
    i=0
    while i<len(l):
        j=i+1
        while j<len(l):
            if not menor(l[i],l[j]):
                j=len(l)+2
            j+=1
        if j==len(l):
            return l[i]
        i+=1
    return l[-1]

def ordenar(l):
    ret=[]
    for i in range(0,len(l)):
        m=encontrarMin(l)
        ret.append(m)
        l.remove(m)
    return ret  

def calcularSucesores(a,acum):
    if a in sucs:
        return sucs[a]
    else:
        return[]

def menor(a,b):
    return not a in sucesores[b]

def esCoherente(l):
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            if not menor(l[i],l[j]):
                return False
    return True
        
f=open("data")

nums=set()
sucs={}

entrada=[]

for l in f:
    entrada+= [l]
f.close()
print(len(entrada))
i=0
for l in entrada:
    if len(l.split("|"))<2:
        i+=1
        break
    a,b=l[0:len(l)-1].split("|")
    a=int(a)
    b=int(b)
    if not a in nums:
        nums.add(a)
        sucs[a]=[b]
    else:
        sucs[a].append(b)
    if not b in nums:
        nums.add(b)
        sucs[b]=[]
    i+=1
    if l=="\n":
        break;
        
sucesores={}
for elem in nums:
    sucesores[elem]=calcularSucesores(elem,set())
ret=0
ret2=0
while i < len(entrada):
    arr=entrada[i][0:len(entrada)-2].split(",")
    arr=[int(a) for a in arr]
    if esCoherente(arr):
        print(arr)
        ret+=arr[(len(arr)-1)//2]
    else:
        l2=ordenar(arr)
        ret2+=l2[(len(l2)-1)//2]
        
    i+=1    
    
print(ret2)

