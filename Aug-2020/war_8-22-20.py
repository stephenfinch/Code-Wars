def summation(num):
	return sum(range(1,num+1))


def solve(s):
	if test(s):
		return 'OK'
	for i in range(len(s)):
		temp = s[:i]+s[i+1:]
		if test(temp):
			return 'remove one'
	else:
		return 'no answer'


def test(s):
	output = True
	for i in range(len(s)):
		if s[i] != s[-1-i]:
			output = False
	return output



print(solve("abba"),"OK")