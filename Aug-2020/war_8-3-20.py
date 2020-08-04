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
#print(solve([[14,2],[0,-16],[-12,-16]]),3584)

def repeat_str(r, s):
	return s*r


def all_non_consecutive(arr):
	output = []
	for i in range(1, len(arr)):
		if arr[i] - arr[i-1] != 1:
			output.append({'i':i, 'n':arr[i]})
	return output

print(all_non_consecutive([1,2,3,4,6,7,8,10]), [{'i': 4, 'n': 6}, {'i': 7, 'n': 10}])