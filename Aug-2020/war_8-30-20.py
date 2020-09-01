letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def missing_alphabets(s):
	s = list(s)
	s.sort()
	output = []
	while s:
		temp_letters = letters.copy()
		for i in range(len(temp_letters)-1, -1, -1):
			if temp_letters[i] in s:
				s.pop(s.index(temp_letters[i]))
				temp_letters.pop(i)
			else:
				output.append(temp_letters[i])
	return ''.join(sorted(output))

#print(missing_alphabets("abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy"),"ayzz")

def divisors(num):
	output = []
	for x in range(2, num):
		if num % x == 0:
			output.append(x)
	if output:
		return output
	return str(num)+' is prime'