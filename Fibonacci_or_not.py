n=int(input())
a=0
b=1
c=0
for i in range(2,n+1):
    sum=a+b
    b=a
    a=sum
    if(n==sum):
        print("True")
        c=1
if(c==0):
    print("False")