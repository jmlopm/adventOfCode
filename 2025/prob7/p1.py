def vueltaAtras(test,current,arr):
    if arr==[]:
        return current==test
    else:
        if vueltaAtras(test,current*arr[0],arr[1::]):
            return True
        if vueltaAtras(test,current+arr[0],arr[1::]):
            return True
    return False
        

def resolver(test,arr):
    res=arr[0]
    return vueltaAtras(test, res, arr[1::])

ret=0
f=open("data")
for l in f:
    a,b=l.split(":")
    test=int(a)
    b=b.replace("\n","")
    b=[int(elem) for elem in b[1::].split(" ")]
    if resolver(test,b):
        ret+=test
        
print(ret)