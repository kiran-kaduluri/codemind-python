def is_automorphic(n):
    square = n**2
    str_n = str(n)
    str_square = str(square)
    if str_square.endswith(str_n):
        return True
    return False

num = int(input())
if is_automorphic(num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")