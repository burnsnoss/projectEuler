# project euler problem 3
# largest prime factor of the number 600851475143

big_number = 600851475143

def getFactors(n):
	# returns a list of factors of n
	# if it returns just [1, n], then it's prime
	# should probably write another function that would take less time
	#  to determine just if a number is prime, like isPrime()
	i = 2
	fs = [1]  # factors list
	target = n
	while i < target:
		if n % i == 0:
			fs.append(i)
			target = n / i
		i += 1

	i = -1
	len_factors = -1 * len(fs)
	fs2 = []
	while i >= len_factors:
		fs2.append(n/fs[i])
		i -= 1

	return fs + fs2


def getPrimes(x = 1, n = 10):
	# returns a list of prime numbers beginning with the next prime after x
	# returns n total primes
	# probably a brute force tactic here
	x += 1
	p = []
	while len(p) < n:
		if len(getFactors(x)) == 2:
			p.append(x)
		x += 1

	return p


def getNextPrime(x):
	p = getPrimes(x, 1)
	return p[0]



if __name__ == '__main__':
	# BRUTE FORCE TACTICS:
	# find all factors of this number and find the greatest one that is prime
	# O(n^2) it seems
	# BETTER TACTIC:
	# get list of primes
	# divide by primes starting with 2 
	# if it is a factor, change target number to other factor and continue

	
	# get first 100 primes
	# primes = getPrimes(1, 100)

	# jk were gonna just start at 2 and get the next prime as we go


	# go through list of primes and do the prime factorization algo
	current = big_number 
	p = 2
	factors = []
	while True:
		if current % p == 0:
			current = current / p
			factors.append(p)
		else:
			p = getNextPrime(p)

		if current == p:
			factors.append(p)
			break


	print(factors)
	exit()

