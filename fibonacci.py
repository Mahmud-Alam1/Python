def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci_series(num):
    for i in range(num):
        print(fib(i), end=" ")

num=int(input("Enter the item:-"))
print(num)
fibonacci_series(num)
