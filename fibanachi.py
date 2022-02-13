fib_array = []

def fib(n):
    if n < 2:
        return n 
    return fib(n-1) + fib(n-2)

for i in range(12):
    fib_array.append(fib(i))

print(fib_array)