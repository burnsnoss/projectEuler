''' 
project euler problem 10 - burnsnoss - 9/4/2021
sum of primes below 2 million
'''

import time
from util import eratosthenes


if __name__ == '__main__':
	tic = time.clock()

	# use sieve of eratosthenes, then sum
	n = 2000000
	primes = eratosthenes(n)
	print(sum(primes))

	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()