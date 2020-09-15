def dup(arr):
	output = []
	for word in arr:
		new_word = word[0]
		for i in range(1,len(word)):
			if word[i] != word[i-1]:
				new_word += word[i]
		output.append(new_word)
	return output

#print(dup(["putteellinen","keenness"]), ['putelinen','kenes'])



import random

def swap(a, b, arr):
	temp_val = arr[a]
	arr[a] = arr[b]
	arr[b] = temp_val
	return arr

def sort_items(arr):
	for i in range(len(arr)-1):
		for i in range(1, len(arr)):
			if arr[i] > arr[i-1]:
				arr = swap(i, i-1, arr)
		temp_list = [x.show() for x in arr]
		print(temp_list)
			

class Item:
	
	def __init__(self, size):
		self.size = size
		self.char = {0: '|', 1: '||', 2: '|||', 3: '||||'}

	def __gt__(self, other):
		if self.size > other.size:
			return True
		return False

	def show(self):
		return self.char.get(self.size)



lst = [Item(random.randint(0,3)) for x in range(20)]

sort_items(lst)