def pan(n):
    s=0
    t=n
    while(n):
        s=s*10+(n%10)
        n//=10
    if(t==s):
        return 1
    return 0
def prime(n):
    if(n==1):
        return 0
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return 0
    return 1
n=int(input())
c=1
while(1):
    if(prime(c+n) and pan(c+n)):
        print(n+c)
        break
    c+=1