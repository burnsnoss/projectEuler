''' 
project euler problem 21 - burnsnoss - 10/19/2021
amicable numbers
'''

import time
from util import getFactors

# use my getFactors function to get the factors of a, 
# then sum_factors(a) = b; getFactors of b,
# check sum_factors(b) = a, if yes, is amicable
# also check a != b


if __name__ == '__main__':
	tic = time.clock()
	
	n = 10000

	amicables = []

	for a in range(1, n):
		factors_a = getFactors(a)
		factors_a.pop(-1)
		b = sum(factors_a)
		if a == b:
			continue

		factors_b = getFactors(b)
		factors_b.pop(-1)

		if a == sum(factors_b) and a not in amicables and b not in amicables:
		# 	total += a + b
			amicables.append(a)
			amicables.append(b)


	print(sum(amicables))

	
	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()