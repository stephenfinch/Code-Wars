def is_divisible(n,x,y):
	return n % x == 0 and n % y == 0


def halving_sum(n):
	den, num = 2, n
	while round(n/den) > 1:
		num += round(n/den)
		den = den*2
		print(den, num)
	return num

print(halving_sum(25),47)