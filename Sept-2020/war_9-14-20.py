def dup(arr):
	output = []
	for word in arr:
		new_word = word[0]
		for i in range(1,len(word)):
			if word[i] != word[i-1]:
				new_word += word[i]
		output.append(new_word)
	return output

print(dup(['aaabbtee', 'akleekbwq']), [])
print(dup(["putteellinen","keenness"]), ['putelinen','kenes'])