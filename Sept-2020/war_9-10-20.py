def add(num1, num2):
	num1, num2, output, index = list(str(num1)), list(str(num2)), [], 0
	while num1 and num2:
		output.insert(0, str(int(num1.pop(-1)) + int(num2.pop(-1))))
	left_over = num1 + num2
	output = left_over + output
	return int(''.join(output))

print(add(1111580,34523))