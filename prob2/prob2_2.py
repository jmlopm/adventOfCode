path="C:/Users/josem/Desktop/AoC/2026/prob2/"

def suma(a,b):
    return (b-a+1)*(a+b)//2

invalidList=set()

def iteraI(n,i):
    ret=0
#len(str(n))//i es la longitud del fragmento
    fragment=int(str(n)[0:len(str(n))//i])
    return sum([fragment*10**((len(str(n))//i)*j) for j in range(0,i)])

#i es el numero de trozos en los que parto
def isInvalid(n):
    for i in range(2,len(str(n))+1):
        if len(str(n))%i!=0:
            pass
        else:
            aux=iteraI(n,i)
            if aux==n:
                return True
    return False


f=open(path+"data","r")

intervals=f.readline().split(",")
cont=0
for i in intervals:
    a,b=i.split("-")
    a=int(a)
    b=int(b)
    current=a
    while current<=b:
        if isInvalid(current):
            cont+=current
        current+=1
print(cont)
f.close()