
def increasing(l):
    for i in range(0, len(l)-1):
        if l[i+1]<=l[i]:
            return False
    return True

def decreasing(l):
    return increasing(l[::-1])

def noBigDifferences(l):
    for i in range(0, len(l)-1):
        if abs(l[i]-l[i+1])>3:
            return False
    return True
    

def isSafe(l):
    if (increasing(l) or decreasing(l)) and noBigDifferences(l):
        return True
    else:
        return False

def resolver(l):
    arr=[int(a) for a in l[0:len(l)-1].split(" ")]
    if isSafe(arr):
        return True
    else:
        for i in range(0, len(arr)):
            if isSafe(arr[0:i]+arr[i+1::]):
                return True
        return False
    
f=open("data")
ret=0
for l in f:
    if resolver(l):
        ret+=1

print(ret)