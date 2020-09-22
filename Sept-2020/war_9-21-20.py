def solution(value):
	output, value = '00000', str(value)
	for i in range(len(value)):
		print(value[i])
		output += value[i]
	return 'Value is ' + output[len(output)-5:]

print(solution(1204), 'Value is 01204')