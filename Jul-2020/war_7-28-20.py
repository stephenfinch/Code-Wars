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
	a, b = arr[0], arr[1]
	return max(max(a)*max(b),min(a)*min(b))