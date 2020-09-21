
def triangle(row):
	while len(row) > 1:
		temp_row,  = ''
		for i in range(0, len(row) - 2):
			  temp_row += 'RGB'.replace(row[i]).replace(row[i+1])
		row = temp_row
	return row



'''
Colour here:        G G        B G        R G        B R
Becomes colour:      G          R          B          G
'''


print('ABC'.replace('B', '').replace('A', ''))