path="C:/Users/josem/Desktop/AoC/2026/prob2/"

def suma(a,b):
    return (b-a+1)*(a+b)//2

#a y b tienen que tener la misma longitud
def sumasim(a,b):
    return (10**(len(str(a)))+1)*suma(a,b)

def aux(a,b):
    ma=a[0:len(a)//2]
    mb=b[0:len(b)//2]
    aa=int(ma+ma)
    bb=int(mb+mb)
    ret=0
    if aa<int(a):
        ret-=aa
    if bb>int(b):
        ret-=bb
    ma=int(ma)
    mb=int(mb)
    lena=len(str(ma))
    lenb=len(str(mb))
    while lena<lenb:
        ret+=sumasim(ma,int("9"*len(ma)))
        ma=int("1"+"0"*len(ma))
        lena=len(str(ma))
    if lena==lenb:
        ret+=sumasim(ma,mb)
    return ret

f=open(path+"data","r")

intervals=f.readline().split(",")
cont=0
for i in intervals:
    if len(i)>=2:
        a,b=i.split("-")
        if len(a)==len(b) and len(a)%2==1:
            pass
        else:
            if len(a)%2==1:
                a=str(10**(len(a)))
            if len(b)%2==1:
                b=str(10**(len(b)-1)-1)
            print(i,a,b,len(a),len(b))
            cont+=aux(a,b)
            print(cont)
print(cont)
f.close()