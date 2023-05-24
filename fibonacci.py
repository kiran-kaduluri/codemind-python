def fibonacci_series(n):
    a, b = 0, 1

    if n == 1:
        print(a,end=" ")
    else:
        print(a,end=" ")
        print(b,end=" ")

        for _ in range(2, n):
            c = a + b
            print(c,end=" ")
            a, b = b, c

num_terms = int(input())

fibonacci_series(num_terms)