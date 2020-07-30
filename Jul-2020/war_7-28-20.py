def consecutive_sum(num):
	output = []
	for x in range(1,num+1):
		temp = []
		for i in range(x,num+1):
			if sum(temp) == num and temp not in output:
				output.append(temp)
			elif sum(temp) < num:
				temp.append(i)
			else:
				break
	return len(output) + 1


print(consecutive_sum(15), 4)

def solve(arr):
	a, b = [], []
	for item in arr:
		a.append(max(item))
		b.append(min(item))
	a.sort()
	b.sort()
	return max(a[-1]*a[-2], b[0]*b[1])


print(solve([[14,2],[0,-16],[-12,-16]]),3584)
