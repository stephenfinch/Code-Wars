def capitalize(s,ind):
	s = list(s)
	for num in ind:
		try:
			s[num] = s[num].upper()
		except:
			pass
	return ''.join(s)

#print(capitalize("abcdef",[1,2,5]),'aBCdeF')

def solve(a):
	even, odd = 0, 0
	for item in a:
		if type(item) == int:
			if item % 2 == 0:
				even += 1
			else:
				odd += 1
	return even-odd