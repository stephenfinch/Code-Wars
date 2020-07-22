def solve(arr):
	arr.sort()
	if sum(arr[:-1]) < arr[-1]:
		return sum(arr[:-1])
	elif arr[0] > arr[-1]-arr[1]:
		return arr[-1]



print(solve([1,1,1]), 1)
print(solve([1,2,1]), 2)
print(solve([8,2,8]), 9)
print(solve([7,4,10]), 10)
print(solve([12,12,12]), 18)