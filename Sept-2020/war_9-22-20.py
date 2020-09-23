def arr(n=0):
	return [x for x in range(n)]


import random

def squares(n):
	return [x**2 for x in range(1, n+1)]

def num_range(n, start, step):
	return [x for x in range(start, start+(n*step), step)]

def rand_range(n, mn, mx):
	return [random.randint(mn, mx) for x in range(n)]

def primes(n):
	num, nums = 2, []
	while len(nums) < n:
		if all(num%i!=0 for i in range(2,num)):
			nums.append(num)
		num += 1
	return nums