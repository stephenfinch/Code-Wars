def get_middle(s):
	while len(s) > 2:
		s = s[1:-1]
	return s


def high_and_low(numbers):
	numbers = numbers.split(' ')
	numbers = [int(x) for x in numbers]
	return str(max(numbers))+' '+str(min(numbers))