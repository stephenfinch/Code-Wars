def solve(s):
	v, count, totals = 'aeiou', 0, []
	for char in s:
		if char in v:
			count += 1
		else:
			totals.append(count)
			count = 0
	return max(totals)


import random

class Card:
	def __init__(self, level, subject, title, text):
		# Shown Attributes
		self.level = level
		self.subject = subject
		self.title = title
		self.text = text

		# Hidden Attributes
		self.date_created = ''
		self.card_id = 00000
		self.total_study_time = 0

	def delete_card(self):
		pass

	def edit_title(self, new_title):
		self.title = new_title

	def edit_text(self, new_text):
		self.text = new_text

	def study_game(self):
		body_words = self.text.split(' ')
		for i in range(len(body_words)):
			if random.randint(0,3) < 1:
				body_words.pop(i)
		return body_words