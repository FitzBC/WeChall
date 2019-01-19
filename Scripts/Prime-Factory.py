import math
import hashlib
def judge(num):
    for i in range(1,int(math.sqrt(num))+1):
        if(num%i==0 and i!=1):
            return 0
    return 1
def sumdit(num):
    sumall=0
    while(num):
        temp=num%10
        sumall=sumall+temp
        num=math.floor(num/10)
    return sumall
i=1000000
a=0
b=0
while(1):
    i=i+1
    ttt=judge(i)
    if(ttt and a==0):
        if(judge(sumdit(i))):
            a=i
            continue
    if(ttt and a!=0 and b==0):
        if(judge(sumdit(i))):
            b=i
            continue
    if(a!=0 and b!=0):
        break
print(a,b)
a=hashlib.md5((str(a)+str(b)).encode())
print(a.hexdigest())