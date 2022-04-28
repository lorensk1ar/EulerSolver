import random

## MY SLOW FUNCTION
def is_prime(x):
    '''
    IN: integer greater than or equal to 2
    OUT: True if prime, False if composite
    EG: 4 --> False, 5 --> True, 6 --> False
    '''
    # assume number is prime
    prime = True

    # check each number up to but not including x
    i = 2
    while i < x:

        # if any number divides evenly
        if x % i == 0:

            # update result
            prime = False

            # and stop checking
            break

        # increment
        i += 1
        
    return prime

def biggest_factor(x):
    '''
    IN: integer greater than or equal to 2
    OUT: integer representing the biggest prime factor of x
    EG: 4 --> 2, 5 --> 5, 6 --> 3
    '''
    
    # remember biggest factor found so far
    big = 1

    # check each number up to and including x
    for i in range(2, x + 1):
        
        # is the number a divisor?
        if x % i != 0:
            continue
 
        # is the divisor prime?
        prime = is_prime(i)

        # update biggest factor
        if prime:
            big = i

    return big

## YOUR QUICK FUNCTION
def get_primes(n):
    primes = {2: True}

    for i in range(3, n + 1, 2):
        primes[i] = True
        
    m = pow(n, 1/2)
    m = int(m)

    for i in range(3, m + 1, 2):
        if primes[i]:
            j = i 
            while i * j <= n:
                primes[i * j] = False
                j += 2
    return primes

def fast_factor(n):
    m = pow(n, 1/2)
    m = int(m)

    big = 1
    e = 0
    while n % 2 == 0:
        n /= 2
        big = 2

    for f in range(3, m + 1, 2):
        if primes[f]:
            e = 0
            while n % f == 0:
                n /= f
                big = f

    if n > 1:
        n = int(n)
        big = n

    return big

## MAIN
import time
start = time.time()

top = 10**5
stop = int(pow(top,1/2))
primes = get_primes(stop)
print("I know kung fu!")
print()

ok = True

# Start with 1 test
for test in range(10**5):

    x = random.randint(2, top+1)

    brute = biggest_factor(x)
    quick = fast_factor(x)
    if quick != brute:
        ok = False
        print(x)
        print(brute)
        print(quick)
        print()

if ok:
    print("Yup!")
else:
    print("Nope!")

end = time.time()
print(str(round(end - start, 3)) + "s")
