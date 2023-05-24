x=int(input())
y=int(input())
i=x
for r in range(x,y+1):
    q=r
    while r!=0:
        s=r%10
        r=r//10
        if s==0:
            break
        if q%s!=0:
            break
    else:
        print(q,end=" ")