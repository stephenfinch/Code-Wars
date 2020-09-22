def solution(value):
	output = '00000'
	for i in range(len(value), 0, -1):
		output[i] = value[i]
	return output