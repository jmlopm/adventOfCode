import re

def resultado(mul):
    aux=mul.split("mul")[1]
    aux=aux[1:len(aux)-1]
    a,b=aux.split(",")
    return int(a)*int(b)

pattern=r"mul\([0-9]{1,3},[0-9]{1,3}\)"
ret=0
f=open("data")
for l in f:
    matches=re.findall(pattern,l)
    for m in matches:
        ret+=resultado(m)

print(ret)