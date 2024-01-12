import math

def check(x):
    if (x<2):
        return False
    for n in range(2, math.ceil(math.sqrt(x))+1):
        
        if (x%n == 0) and (x!=n):
            return False
    return True


def primes(y):
    for x in range(y):
        if(check(x)):
            print(x, end=' ')


primes(30)