'''
def solve(arr):
	i = 0
	while len(arr) > 1:
		arr.sort()
		arr[-1] -= 1
		arr[0] -= 1
		if arr[0] <= 0:
			arr = arr[1:]
		if arr[-1] <= 0:
			arr = arr[:-1]
		i += 1
	return i
'''
import math
def solve(arr):
	arr.sort()
	if sum(arr[:-1]) < arr[-1]:
		return sum(arr[:-1]), '==============='
	return math.floor(((arr[-1]+arr[0])+arr[1])/2)


print(solve([1,1,1]), 1)
print(solve([1,2,1]), 2)
print(solve([8,2,8]), 9)
print(solve([7,4,10]), 10)
print(solve([12,12,12]), 18)