''' 
project euler problem 8 - burnsnoss - 9/2/2021
finding largest 13-factor product in list of integers
'''

import time

if __name__ == '__main__':
	tic = time.clock()

	# read input file
	fs = open('p8_input.txt', 'r')
	digits = []
	for line in fs:
		txt = line.strip('\n')
		for c in txt:
			digits.append(int(c))

	greatest = 0
	# iterate over digits
	for i in range(0, len(digits) - 12):
		# get the next thirteen digits
		factors = digits[i:i+13]
		product = 1
		# multiply them together
		for f in factors:
			product *= f

		# check if its greater than what we got
		if product > greatest:
			greatest = product

	print(greatest)

	toc = time.clock()
	print(f'time: {(toc - tic):.4f}')
	exit()