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
	arr.sort()
	print(arr)
	if arr[2]-arr[0] < arr[1]:
		return arr[2]
	else:
		return arr[1]


print(solve([1,1,1]), 1)
print(solve([7,4,10]), 10)