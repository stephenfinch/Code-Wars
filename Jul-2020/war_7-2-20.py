def multiples(m, n):
	output = []
	for i in range(1, m+1):
		output.append(n*i)
	return output



def likes(names):
	if len(names) > 3:
		return f'{names[0]}, {names[1]}, and {len(names)-2} others like this'
	elif len(names) > 2:
		return f'{names[0]}, {names[1]}, and {names[2]} like this'
	elif len(names) > 1:
		return f'{names[0]} and {names[1]} like this'
	elif len(names) > 0:
		return f'{names[0]} like this'
	else:
		return 'no one likes this'

