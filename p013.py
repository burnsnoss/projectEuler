''' 
project euler problem 13 - burnsnoss - 9/8/2021
sum of a bunch of 50-digit numbers
'''

import time

class AddingMachine:
	terms = []
	total = ''
	max_digits = 0

	def __init__(self, n):
		# pass in a list of strings representing numbers
		self.terms = n
		# set max_digits by checking each term length
		for t in self.terms:
			self.max_digits = max(self.max_digits, len(t))
		return

	def printTerms(self):
		for t in self.terms:
			print(t)
		return

	def sigma(self):
		if self.terms == []:
			return 0

		min_idx = -1 * self.max_digits
		carry = 0
		final = ''
		for i in range(-1, min_idx - 1, -1):
			col_total = 0
			for t in self.terms:
				if (-1 * len(t)) > i:
					# this means the term is shorter than the current digit idx
					# aka there's nothing to add from the current term
					continue
				col_total += int(t[i])

			# "carry the whatever"
			col_total += carry
			# split off last digit of column total
			col_total_str = str(col_total)
			final = col_total_str[-1] + final
			# set carry with remaining digits
			carry = int(col_total_str[:-1])

		final = str(carry) + final
		self.total = final
		return self.total


if __name__ == '__main__':
	tic = time.clock()

	fo = open('p013_input.txt', 'r')

	numbers = []
	for line in fo:
		numbers.append(line.strip('\n'))

	am = AddingMachine(numbers)
	final_answer = am.sigma()
	print(final_answer[:10])


	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()