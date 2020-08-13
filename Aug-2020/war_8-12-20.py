def longest_repetition(s):
	letters = [[s[0], 1]]
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			letters[-1][0] = s[i]
			letters[-1][1] += 1
		else:
			letters.append([s[i], 1])
	biggest = ['', 0]
	for item in letters:
		if item[1] > biggest[1]:
			biggest = item
	return biggest

print(longest_repetition("aaaabb"), ('a', 4))
print(longest_repetition("bbbaaabaaaa"), ('a', 4))
print(longest_repetition("cbdeuuu900"), ('u', 3))
print(longest_repetition("abbbbb"), ('b', 5))