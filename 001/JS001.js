// O(N) SOLUTION
function sum_if_divisable (limit, divisors) {
  let sum = 0;
  
  for (let i = 1; i < limit; i++) {
    const divide = (divisor) => i % divisor == 0;
    const divisable = divisors.some(divide);
    if (divisable) {
      sum += i;
    };
  }; 
  return sum;
};

var limit = 1000;
var divisors = [3, 5]
var answer = sum_if_divisable (limit, divisors);
console.log(answer);

// O(1) SOLUTION
function gcd (a, b) {
  while (b != 0) {
    let t = b;
    b = a % b;
    a = t;
  };
  return a;
};

function lcm (a, b) {
  let d = gcd(a, b);
  return (a * b / d);
};

function gauss_sum (n) {
  return n * (n + 1) / 2;
};

function sum_with_any_two_divisors (limit, a, b) {
  // up to but not including limit
  limit -= 0.000000001;
  
  // declare variable for sum
  let sum = 0;
  
  // 
  const divisors = [a, b, -a * b];
  divisors.forEach (function (divisor) {
    let n = Math.floor(Math.abs(limit / divisor));
    sum += divisor * gauss_sum(n);
  });
  
  return sum;
};

answer = sum_with_any_two_divisors(limit, 3, 5)
console.log(answer);
