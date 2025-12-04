path="C:/Users/josem/Desktop/AoC/2026/prob3/"

f=open(path+"data")

def maxi(vec):
    m=0
    pos=0
    for n in range(0,len(vec)):
        if vec[n]>m:
            m=vec[n]
            pos=n
    return m,pos


suma=0
for l in f:
    case=[]
    for n in l:
        if n!="\n":
            case+=[int(n)]
    start=0
    current=0
    for i in range(0,12):
        m,p=maxi(case[start:len(case)-11+i])
        start+=p+1
        current=current*10+m
    print(current)
    suma+=current

print(suma)
f.close()