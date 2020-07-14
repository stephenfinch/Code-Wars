def is_divisible(n,x,y):
	return n % x == 0 and n % y == 0

def halving_sum(n):
	num = n
	while len(str(n/2)) != 1:
		num += n/2
		n = n/2
	return num