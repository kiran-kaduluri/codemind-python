def reverse(n):
    reversed_num = int(str(abs(n))[::-1])
    if n < 0:
        reversed_num *= -1
    return reversed_num

num = int(input())
rev = reverse(num)
print(rev)
