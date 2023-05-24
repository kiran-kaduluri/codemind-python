n = int(input())
arr = input()
l = list(map(int,arr.split(' ')))
odd=l[1::2]
even=l[::2]
if sum(even)-sum(odd)==0:
    print("YES")
else:
    print("NO")
