def mirror(data: list) -> list:
	return sorted(data) + sorted(data)[::-1][1:]



test = [3,5,3,2,5,6,3,2]
print(mirror(test))