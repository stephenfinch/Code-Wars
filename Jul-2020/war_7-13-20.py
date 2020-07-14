def is_divisible(n,x,y):
	return n % x == 0 and n % y == 0

def halving_sum(n):
	num = n
	while '.' in str(n/2):
		print(n/2)
		num += n/2
		n = n/2
	return num

print(halving_sum(25),47)