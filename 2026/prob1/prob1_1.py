path="C:/Users/josem/Desktop/AoC/prob1/"
f=open(path+"data",'r')

count=0
current=50
for l in f:
    dir=l[0]
    cant=int(l[1::])
    if dir=="L":
        current-=cant
    elif dir=="R":
        current+=cant
    current=current%100
    if current==0:
        count+=1
    
print(count)

f.close()