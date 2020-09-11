def add(num1, num2):
	num1, num2, output = list(str(num1)), list(str(num2)), []
	while num1 and num2:
		output.insert(0, str(int(num1.pop(-1)) + int(num2.pop(-1))))
	if num1 or num2:
		output.insert(0, max(num1, num2)[0])
	return int(''.join(output))

print(add(122,81), 1103)