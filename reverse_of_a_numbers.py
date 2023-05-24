def reverse_integer(n):
    reversed_num = int(str(abs(n))[::-1])
    if n < 0:
        reversed_num *= -1
    return reversed_num

# Example usage
num = int(input())
reversed_num = reverse_integer(num)
print(reversed_num)
