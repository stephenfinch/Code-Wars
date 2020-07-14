def is_divisible(n,x,y):
	return n % x == 0 and n % y == 0

import math
def halving_sum(n):
	den, num = 2, n
	while math.floor(n/den) >= 1:
		num += math.floor(n/den)
		den = den*2
	return num

print(halving_sum(25),47)