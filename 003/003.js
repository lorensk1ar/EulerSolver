const prime_lookup = {0: false, 1: false}
  
function is_prime(n, prime_lookup) {
  prime_lookup = prime_lookup || {};

  if (n in prime_lookup) {
    return (prime_lookup[n])
  } 
  
  else {
    sqrt = Math.floor(Math.sqrt(n))
    
    let i = 0;
    let p = prime_list[i];
    while (p <= sqrt) {
      if (n%p==0) {
        return false
      }
      i++;
      p = prime_list[i];  
    }
    return true  
  }
}

limit = 2000000;
for (i=2; i<=limit; i++) {
  prime_lookup[i] = true;
}

for (let i=2; i<=limit; i++) {
  if (prime_lookup[i]) {
    j = 2;
    while (i * j <= limit) {
      prime_lookup[i*j] = false;
      j++;
    }
  }
}

total = 0
prime_list = [];
for (let i=2; i<=limit; i++) {
  if (prime_lookup[i]) {
    prime_list.push(i);
    total += i
  }
}

console.log(total)
