# straightforward implementation
def sum_if_divisible(limit, a = 3, b = 5):
	total = 0
	for i in range(limit):
		if i % a == 0 or i % b == 0:
			total += i
	return total
# general solution that takes a list of divisors as input
def sum_many_divisors(limit, divisors):
	# initialize list with integer indices and value zero
	numbers = [0 for i in range(limit)]
	# loop through divisors
	for d in divisors:
		k = 1
		multiple = d * k
		
		# loop through multiples less than limit
		while multiple < limit:
			
			# if multiple, include in sum
			numbers[multiple] = multiple
			
			# increment
			k += 1
			multiple = d * k
			
	# return sum
	return sum(numbers)
# constant time solution using Gauss's trick
def sum_if_divisible(limit, a , b):
	# up to but not including limit
	limit -= 0.000000001
	
	# initialize variable for sum
	total = 0
	# add integers divisable by first factor
	n = int(limit / a)
	total += a * n * (n + 1) / 2
	# add integers divisable by second factor
	n = int(limit / b)
	total += b * n * (n + 1) / 2
	# subtract duplicates divisable by both factors
	c = a * b
	n = int(limit / c)
	total -= c * n * (n + 1) / 2
	return total
# returns greatest common divisor using Euclid's algorithm
def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a 
# returns least common multiple
def lcm(a, b):
	c = gcd(a, b)
	return a * b / c
# extends constant time Gauss summation to any two divisors
def sum_any_two_divisors(limit, a, b):
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

# and because everyone loves a good one liner...
print(sum([n if any([n % 3 == 0, n % 5 == 0]) else 0 for n in range(1000)]))
