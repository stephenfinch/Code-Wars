def triangle(row):
	count = 0
	while len(row) > 1:
		temp_row = ''
		for i in range(0, len(row) - 1):
			if row[i] == row[i+1]:
				temp_row += row[i]
			else:
				temp_row += 'RGB'.replace(row[i], '').replace(row[i+1], '')
		row = temp_row
		print(' '*(count//2) + row)
		count += 1
	return row


print(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')