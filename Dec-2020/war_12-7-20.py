import math
def sum_square_even_root_odd(nums):
	# if even - square
	# if odd - root
	return round(sum([x**2 if x%2==0 else math.sqrt(x) for x in nums]), 2)


print(sum_square_even_root_odd([2,2,2,2,2,3,3]))