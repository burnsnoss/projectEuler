''' 
project euler problem 7 - burnsnoss - 9/1/2021
find the 10001st prime
'''

import time

upper_limit = 5000**2

def initPrimeBook(n):
	# book of numbers, key is number, value is bool
	# value is True if prime
	# generates a book with values of True for numbers up to, not including, n
	book = {}
	for i in range(2, n):
		book[i] = True
	return book


def sieveOfEratosthenes(n):
	# my idea here is to generate a dictionary where
	# key = number
	# value = bool (prime or not prime) 
	# book = initPrimeBook(n)
	book = [True] * (n + 1)
	i = 2
	p = []
	while i < n:
		# add i to primes list
		p.append(i)

		# mark all multiples of i as False
		j = i + i
		while j < n:
			book[j] = False
			j += i

		# increment i and then check for the next True
		# this is the next prime
		i += 1
		while i < n and not book[i]:
			i += 1

	return p


if __name__ == '__main__':
	tic = time.clock()
	primes = sieveOfEratosthenes(upper_limit)
	print(primes[10000])  # list indexing: 10001st value is 10000th index
	toc = time.clock()
	print(toc - tic)
	exit()