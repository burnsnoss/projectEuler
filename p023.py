''' 
project euler problem 23 - burnsnoss - 10/20/2021
sum of all numbers that arent the sum of two abundant numbers
'''

import time
from util import getFactors

def getAbundantNumbers(n):
	''' gets abundant numbers below n '''

	abundants = []
	for i in range(1, n):
		factors = getFactors(i, True)
		if sum(factors) > i:
			abundants.append(i)
		
	return abundants


def abundantSieve(n, abundants):
	sieve = [0 for x in range(n)]

	ab_copy = abundants.copy()

	for a in abundants:
		for b in ab_copy:
			# if we are greater than n, no point in adding any more
			if a + b >= n:
				break
			sieve[a+b] = 1

		# pop the first number from ab_copy, we already checked it
		ab_copy.pop(0)

	return sieve


if __name__ == '__main__':
	tic = time.clock()

	# my idea is to just 
	# 1. find all abundant numbers below 28124
	#   - will have to use the getfactors function
	# 2. add the abundant numbers together in pairs
	# 3. check the remaining numbers, add them up
	#   - do like a sieve list thing

	n = 28124

	abundants = getAbundantNumbers(n)

	# there are 6965 abundant numbers, which means adding them together in pairs
	# (binomial coefficient?) will result in 24259095 pairs (i think)
	# we can probably reduce this number, but will it be significant?

	sieve = abundantSieve(n, abundants)

	# sum up the false values in sieve
	total = 0 
	for i in range(1, len(sieve)):
		if not sieve[i]:
			total += i

	print(total)

	# this solution takes a whole second and a half ):
	
	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()