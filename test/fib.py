def fib(n):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case 2:
            return 2
        case _:
            return fib(n-1) + fib(n-2)
        
        
for n in range(30):
    print(fib(n), end=' ')