# straightforward implementation
def sum_if_divisible(limit, a = 3, b = 5):
	total = 0
	for i in range(limit):
		if i % a == 0 or i % b == 0:
			total += i
	return total

# general solution that takes a list of factors as input
def sum_many_factors(limit, factors):
	numbers = [0 for i in range(limit)]

	for factor in factors:
		i = 1
		multiple = i * factor
		while multiple < limit:
			numbers[multiple] = multiple
			i += 1
			multiple = i * factor

	total = sum(numbers)
	return total
