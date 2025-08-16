from math import gcd  
import numpy as np

XD=10000000000000

def isSI(a1,b1,c1,a2,b2,c2):
    if a1==0:
        if a2!=0:
            return False
        else:
            if b1==0:
                if b2!=0:
                    return False
            else:
                return c2!=b2/b1*c1
    else:
        return b2==a2/a1*b1 and c2!=a2/a1*c1

def isINT(a):
    epsilon=0.001
    return abs(round(a)-a)<epsilon

def isSCI(a1,b1,c1,a2,b2,c2):
    if a1==0:
        if a2!=0:
            return False
        else:
            if b1==0:
                if b2!=0:
                    return False
            else:
                return c2==b2/b1*c1
    else:
        return b2==a2/a1*b1 and c2==a2/a1*c1

def resolver(a1,b1,c1,a2,b2,c2):
    if isSI(a1,b1,c1,a2,b2,c2):
        return -1,-1
    if isSCI(a1,b1,c1,a2,b2,c2):
        if b1!=0:
            c=c1/b1
            m=a1/b1
            na=0
            res=c-m*na
            while res>=0:
                if isINT(res):
                    return na,res
                na+=1
                res=c-m*na
            return -1,-1
        else:
            print("aaa")
            if isINT(c1/a1):
                return c1/a1
    else:
        a=np.array([[a1,b1],[a2,b2]])
        b=np.array([c1,c2])
        sol=np.linalg.solve(a,b)
        if isINT(sol[0]) and isINT(sol[1]):
            sol=[round(sol[0]),round(sol[1])]
            return sol
        else:
            return -1,-1


def parseButton(s):
    s2=s.split(":")[1]
    a,b=s2.split(",")
    a=int(a.split("+")[1])
    b=int(b.split("+")[1])
    return a,b
    
    
def parsePoint(s):
    s2=s.split(":")[1]
    a,b=s2.split(",")
    a=int(a.split("=")[1])+XD
    b=int(b.split("=")[1])+XD
    return a,b
    
f=open("data")

ret=0

#entre 35800 y 40000

while line:=f.readline():
    line2=f.readline()
    line3=f.readline()
    line4=f.readline()
    x1,y1=parseButton(line)
    x2,y2=parseButton(line2)
    x, y =parsePoint(line3)
    sol=resolver(x1,x2,x,y1,y2,y)
    print(sol)
    if sol[0]!=-1:
        if sol[0]>=0 and sol[1]>=0:
            ret+=3*sol[0]+sol[1]
        else:
            print(sol,"####")
    
print(ret)    
    