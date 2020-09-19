def solve(s):
	nums = []
	while s:
		temp = ''
		while s[0].isnumeric():
			temp += s[0]
			if len(s) > 1:
				s = s[1:]
			else:
				s = ['a']
		if temp:
			nums.append(int(temp))
		s = s[1:]
	return max(nums)




print(solve('av223esa4vasd19f1'))