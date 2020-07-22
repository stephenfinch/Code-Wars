def solve(arr):
	i = 0

	while len(arr) > 1:
		arr.sort()
		arr.reverse()

		arr[0] -= 1
		arr[-1] -= 1

		if arr[-1] <= 0:
			arr = arr[:-1]
		if arr[0] <= 0:
			arr = arr[1:]
		
		i += 1
	return i


print(solve([1,1,1]), 1)
print(solve([1,2,1]), 2)
print(solve([8,2,8]), 9)
print(solve([7,4,10]), 10)
print(solve([12,12,12]), 18)