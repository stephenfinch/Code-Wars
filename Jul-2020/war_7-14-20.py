def get_middle(s):
	while len(s) > 2:
		s = s[1:-1]
	return s

def high_and_low(numbers):
	numbers = numbers.split(' ')
	for item in numbers:
		numbers.append(numbers.pop(numbers.index(item)))
	return max(numbers), min(numbers)