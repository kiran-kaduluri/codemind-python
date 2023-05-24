n = int(input())
arr = input()
l = list(map(int,arr.split(' ')))
p=1
np=1
c=0
d=0
for i in range(0,n):
    if l[i]==1 or l[i]==2 or l[i]==3:
        p=p*l[i]
    elif l[i]>3:
        c=0
        for j in range(2,l[i]):
            if l[i]%j==0:
                np=np*l[i]
                c=0
                break
            else:
                c=c+1    
        if c>0:
            p=p*l[i]
        
#print("prime",p)
#print("non-prime",np)
print(abs(np-p))