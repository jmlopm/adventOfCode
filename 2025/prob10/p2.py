f=open("data")

arr=[]
mapa={}
for i in range(0,10):
    mapa[i]=[]

zeros=[]
scores=[]
i=0
for l in f:
    case=[]
    case2=[]
    j=0
    for c in l:
        if c!="\n":
            case.append(int(c))
            if c=="0":
                zeros.append([i,j])
            if c=="9":
                case2.append(1)
            else:
                case2.append(0)
            mapa[int(c)].append([i,j])
            j+=1
    arr.append(case)
    scores.append(case2)
    i+=1
    
score=0

dimx=len(arr)
dimy=len(arr[0])

def enRango(i,j,dimx,dimy):
    return i>=0 and j>=0 and i<dimx and j<dimy


for i in range(8,-1,-1):
    for x,y in mapa[i]:
        partialScore=0
        if enRango(x+1,y,dimx,dimy) and arr[x+1][y]==i+1:
            partialScore+=scores[x+1][y]
                
        
        if enRango(x-1,y,dimx,dimy) and arr[x-1][y]==i+1:
            partialScore+=scores[x-1][y]
        
        if enRango(x,y+1,dimx,dimy) and arr[x][y+1]==i+1:
            partialScore+=scores[x][y+1]
        
        if enRango(x,y-1,dimx,dimy) and arr[x][y-1]==i+1:
            partialScore+=scores[x][y-1]
        scores[x][y]=partialScore

for a,b in mapa[0]:
    score+=(scores[a][b])

print(score)
    