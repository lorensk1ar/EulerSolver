### MODULES
import math


### FUNCTIONS
def reduce_by(number, factor):
    remainder = number
    exponent = 0
    while remainder % factor == 0:
        exponent += 1
        remainder /= factor
    return exponent, remainder

def get_primes(n):
    primes = {}

    for i in range(2, n + 1):
        primes[i] = True

    for i in range(2, n + 1):
        if primes[i]:
            j = 2
            while i * j <= n:
                primes[i * j] = False          
                j += 1

    return primes


### MAIN
n = 600851475143

# list all potential prime factors
top = int(math.sqrt(n))
primes = get_primes(top)

# reduce by primes
factors = {}
remainder = n
for factor, is_prime in primes.items():
    if is_prime:
        exponent, remainder = reduce_by(remainder, factor)
        factors[factor] = exponent

    
# any remainder?
if remainder > 1:
    remainder = int(remainder)
    factors[remainder] = 1
         
ans = 1
for factor, exponent in factors.items():
    if exponent > 0 and factor > ans:
        ans = factor

print (ans)
