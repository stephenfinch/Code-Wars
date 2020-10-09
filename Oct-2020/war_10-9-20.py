def unique_in_order(arr):
	output = [arr[0]]
	for i in range(1,len(arr)):
		if arr[i] != output[-1]:
			output.append(arr[i])
	return output


def persistence(n):
	output, count = 1, 0
	while len(str(n)) > 1:
		for x in str(n):
			output *= int(x)
		count += 1
		n = output
		print(count, n)
	return count

def is_in_middle(s):
	s = s.split('abc')
	return len(s[0]) == len(s[1]) or len(s[0]) == len(s[1]) - 1

print(is_in_middle("AabcBB"), True)
print(is_in_middle("AabcBBB"), False)