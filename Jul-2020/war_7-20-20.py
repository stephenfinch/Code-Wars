def solution(a, b):
	if len(str(a)) <= len(str(b)):
		return str(a)+str(b)+str(a)
	else:
		return str(b)+str(a)+str(b)

