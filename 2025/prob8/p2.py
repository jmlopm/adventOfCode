import sys

f=open("data")

def enrango(x,y,dimx,dimy):
    return x>=0 and y>=0 and x<dimx and y<dimy

def computeAntinodes(p1,p2):
    diffx=(p1[0]-p2[0])
    diffy=(p1[1]-p2[1])
    k=0
    ret1=[]
    ret2=[]
    while enrango(p1[0]+k*diffx,p1[1]+k*diffy,dimx,dimy):
        ret1.append([p1[0]+k*diffx,p1[1]+k*diffy])
        k+=1
    k=0
    while enrango(p2[0]-k*diffx,p2[1]-k*diffy,dimx,dimy):
        ret1.append([p2[0]-k*diffx,p2[1]-k*diffy])
        k+=1
    return ret1+ret2
i=0
mapadeantenas={}
for l in f:
    l=l.replace("\n","")
    j=0
    for c in l:
        if l[j]!=".":
            if l[j] in mapadeantenas:
                mapadeantenas[l[j]].append([i,j])
            else:
                mapadeantenas[l[j]]=[[i,j]]
        j+=1
    i+=1
dimx=i
dimy=len(l)
mapadeantinodos=[]
for i in range(0,dimx):
    mapadeantinodos.append([False]*dimy)
cont2=0
cont=0
for ants in mapadeantenas:
    for i in range(0,len(mapadeantenas[ants])):
        for j in range(i+1,len(mapadeantenas[ants])):
            antinodes=computeAntinodes(mapadeantenas[ants][i], mapadeantenas[ants][j])
            for anti in antinodes:
                mapadeantinodos[anti[0]][anti[1]]=True
                
cont=0
i=0
for row in mapadeantinodos:
    j=0
    for elem in row:
        if elem:
            cont+=1
        j+=1
    i+=1
print(cont)