path="C:/Users/josem/Desktop/AoC/prob1/"
f=open(path+"data1",'r')

count=0
current=50
next=50
for l in f:
    dir=l[0]
    cant=int(l[1::])
    next=current
    count+=cant//100
    if current==0:
        if dir=="L":
            next-=cant%100
        elif dir=="R":
            next+=cant%100
    else:
        if dir=="L":
            next-=cant%100
            if next<=0:
                count+=1
        elif dir=="R":
            next+=cant%100
            if next>99:
                count+=1
#se pasa por el 0
    next=next%100
    current=next
print(count)
f.close()