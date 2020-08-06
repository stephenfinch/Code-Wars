def sum_two_smallest_numbers(n):
	n = sorted([x for x in n if x >= 0])
	return sum(n[:2])

def say_hello(name):
	return "Hello, " + name