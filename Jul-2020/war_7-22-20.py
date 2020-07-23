def check_exam(arr1,arr2):
	total = 0
	for i in range(len(arr1)):
		if arr1[i] == arr2[i]:
			total += 4
		elif arr2[i] != "":
			total -= 1
	return total if total >= 0 else 0


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w', 'x', 'y', 'z']
def solve(s):
	output = [0,0,0,0]
	for char in s:
		if char.isdigit():
			output[2] += 1
		elif char in letters:
			output[1] += 1
		elif char.lower() in letters:
			output[0] += 1
		else:
			output[-1] += 1
	return output