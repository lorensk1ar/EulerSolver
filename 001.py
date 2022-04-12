def sum_if_divisible(limit, a = 3, b = 5):
	total = 0
	for i in range(limit):
		if i % a == 0 or i % b == 0:
			total += i
	return total
