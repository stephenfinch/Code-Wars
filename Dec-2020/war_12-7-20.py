import math
def sum_square_even_root_odd(nums):
	return round(sum([x**2 if x%2==0 else math.sqrt(x) for x in nums]), 2)

#print(sum_square_even_root_odd([2,2,2,2,2,3,3]))


def check_password(s):
	_len, upper, lower, digit, special = 7<len(s)<21, False, False, False, False
	for i in set(s):
		if True:
			pass
	return _len

print(check_password('aaaaaaaaggggggggggggg'))