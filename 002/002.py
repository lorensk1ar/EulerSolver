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
