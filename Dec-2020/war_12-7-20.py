import math
def sum_square_even_root_odd(nums):
	return round(sum([x**2 if x%2==0 else math.sqrt(x) for x in nums]), 2)

#print(sum_square_even_root_odd([2,2,2,2,2,3,3]))


def check_password(s):
	_len, upper, lower, digit, special, other = 7<len(s)<21, False, False, False, False, True
	for i in set(s):
		if i.isdigit():
			digit = True
		elif i in '!@#$%^&*?':
			special = True
		elif i.isupper():
			upper = True
		elif i.islower():
			lower = True
		else:
			other = False
	return 'valid' if all([_len, upper, lower, digit, special, other]) else 'not valid'

print(check_password('asdfa4Edfg !aad'))