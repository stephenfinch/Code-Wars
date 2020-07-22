def solve(arr):
	i = 0
	while sum(arr) > 1:
		big, small = 0
		for num in arr:
			if num > big:
				big = num
			if small < num:
				small = num




		arr[arr.index(min(arr))] -= 1
		arr[arr.index(max(arr))] -= 1
		for x in range(len(arr)):
			if arr[x] < 1:
				arr.pop(x)
		print(arr)
		i += 1
	return i


print(solve([1,1,1]), 1)
print(solve([7,4,10]), 10)