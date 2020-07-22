'''
def solve(arr):
	i = 0
	while len(arr) > 1:
		for num in arr:
			if num < 1:
				arr.pop(arr.index(num))
		if len(arr) > 1:
			a = arr.index(max(arr))
			b = arr.index(min(arr[:a]+arr[a:]))
		else:
			return i, '============='

		if a == b:
			return i

		print(arr, a, b)

		arr[a] -= 1
		arr[b] -= 1
		
		i += 1
		return i
'''
def solve(arr):
	i = 0
	arr.sort()
	arr.reverse()
	#print(arr)
	while len(arr) > 1:


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