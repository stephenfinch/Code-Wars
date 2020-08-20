def custom_christmas_tree(chars, n):
	tree = ' ' * (n-1)
	chars = chars * n
	print(chars)
	for i in range(1,n):
		tree += chars[i-1%n]
		tree += '\n'
	return tree


print(custom_christmas_tree("*@o",3),'\n'
"""  *
 @ o
* @ o
  |""")