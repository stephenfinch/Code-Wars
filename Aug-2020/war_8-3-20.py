def solve(arr):
	min_, max_ = [], []
	for item in arr:
		min_.append(min(item))
		max_.append(max(item))
	a, b = 1, 1
	for i in range(len(arr)):
		a *= max_[i]
		b *= min_[i]
	return max(a, b), min_, max_, a, b


print(solve([[14,2],[0,-16],[-12,-16]]),3584)