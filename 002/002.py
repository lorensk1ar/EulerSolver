# Iterative solution to sum even numbers in Fibonacci sequence
def sum_even_fibs(limit):
    e = 0
    f = 1
    total = 0
    while f < limit:
        e, f = f, e + f

        if f % 2 == 0:
            total += f
   
    return total
    
limit = 4000000
ans = sum_even_fibs(limit)
print(ans)


# Constant time solution for ith number in the fibonnacci sequence
Phi = (1 + pow(5, 1/2))/2
phi = (1 - pow(5, 1/2))/2

def get_fib(n):
  f =(pow(Phi, n) - pow(phi, n)) / pow(5, 1/2)
  f = int(f)
  return f 


limit = 4000000
total = 0
i = 1
f = 1
while f < limit:
  print(i, f)

  if f % 2 == 0:
    total += f

  i += 1
  f = get_fib(i)

print("Sum:", total)
