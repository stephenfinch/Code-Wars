v = ['a','e','i','o','u']
def disemvowel(s):
	a = [x for x in s if s not in v]
	return ''.join(a)