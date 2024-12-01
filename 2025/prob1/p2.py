import math

f=open("data")

a=[]
b=[]
for l in f:
    l2=l.split(" ")
    e1,e2=int(l2[0]),int(l2[len(l2)-1])
    a.append(e1)
    b.append(e2)
    
a.sort()
b.sort()

ret=0

for elem in a:
    ret+=elem*b.count(elem)

print(ret)