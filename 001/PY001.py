##  linear time solution with unlimited divisors
# cycle through multiples for each divisor
def sum_if_divisible_with_many_divisors(limit, divisors):
	numbers = [0 for i in range(limit)]

	for d in divisors:
		k = 1
		multiple = d * k
		while multiple < limit:
			numbers[multiple] = multiple
			i += 1
			multiple = d * k

	total = sum(numbers)
	return total


##  constant time solution with any two divisors
# greatest common divisor
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a 

# least common multiple
def lcm(a, b):
	c = gcd(a, b)
	return a * b / c

# gauss summation with any two divisors
def sum_if_divisible_with_any_two_factors(limit, a, b):
	# up to but not including limit
	limit -= 0.000000001

	total = 0

	n = int(limit / a)
	total += a * n * (n + 1) / 2

	n = int(limit / b)
	total += b * n * (n + 1) / 2

	c = lcm(a, b)
	n = int(limit / c)
	total -= c * n * (n + 1) / 2

	return total

## unit test
slow = 0
quick = 0
tick = time.time()

ok = True
for trial in range(1000):
	limit = random.randint(100000, 100000)
	a = random.randint(1, 1000)
	b = random.randint(1, 1000)

	divisors = [a, b]
	x = sum_if_divisible_with_many_divisors(limit, divisors)
	slow += time.time() - tick
	tick = time.time()

	y = sum_if_divisible_with_any_two_factors(limit, a, b)
	quick += time.time() - tick
	tick = time.time()

	if x != y:
		ok = False
		print(limit, x, y, y - x)

if ok:
	print("Rockstar!")
  
print("Time using list:", round(slow, 3), "seconds")
print("Time using Gauss:", round(quick, 3), "seconds")

