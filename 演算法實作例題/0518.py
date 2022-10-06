def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #n * (n - 1)!

print(factorial(4))

#fibonacci數列
#f(n) = f(n - 1) + f(n - 2)
#f(0) = 0, f(1) = 1