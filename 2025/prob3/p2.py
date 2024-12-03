import re

do="do()"
dont="don't()"
pattern=r"mul\([0-9]{1,3},[0-9]{1,3}\)"

def findNextDo(startingPos, l):
    for i in range(startingPos, len(l)-3):
        if l[i:4]==do:
            return i

def resultado(mul):
    aux=mul.split("mul")[1]
    aux=aux[1:len(aux)-1]
    a,b=aux.split(",")
    return int(a)*int(b)



f=open("data")
ret=0
caso=""
for l in f:
    caso+=l
matches=[]
aux=caso.split(dont)
matches=re.findall(pattern,aux[0])
for i in range(1,len(aux)):
    aux2=aux[i].split(do)
    for i in range(1,len(aux2)):
        matches+=re.findall(pattern,aux2[i])
for m in matches:
    ret+=resultado(m)
print(ret)
f.close()