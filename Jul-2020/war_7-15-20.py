def solve(arr):
	new_arr = []
	for i in range(len(arr)):
		if arr[-1-i] not in new_arr:
			new_arr.append(arr[-1-i])
	new_arr.reverse()
	return new_arr