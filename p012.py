''' 
project euler problem 12 - burnsnoss - 9/6/2021
first triangle number to have over 500 divisors
'''

import time
from util import getFactors



if __name__ == '__main__':
	tic = time.clock()

	# calculate the triangle numbers by just adding the next index
	# getFactors for each one, EZ
	i = 1           # index of triangle number
	tri_number = 0  # triangle number value
	while True:
		tri_number += i
		factors = getFactors(tri_number)
		if len(factors) > 500:
			print(tri_number)
			break

		i += 1

	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()