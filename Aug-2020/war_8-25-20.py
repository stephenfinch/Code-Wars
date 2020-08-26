v = ['a','e','i','o','u']
def disemvowel(s):
	return ''.join([x for x in s if x.lower() not in v])