'''
utility class for project euler problems
''' 

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


def eratosthenes(n):
	# perform sieve up to n
	# return list of primes p
	book = [True] * (n + 1)
	i = 2
	p = []
	while i < n + 1:
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


# adds up a list of numbers passed to it
# numbers must be in string form, in a list
def sigma(terms = []):
		if terms == []:
			return 0

		if len(terms) == 1:
			return terms[0]

		# get max number of digits of terms
		max_digits = 0 
		for t in terms:
			max_digits = max(max_digits, len(t))

		min_idx = -1 * max_digits
		carry = 0
		final = ''
		for i in range(-1, min_idx - 1, -1):
			col_total = 0
			for t in terms:
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
			if col_total_str[:-1] != '':
				carry = int(col_total_str[:-1])
			else:
				carry = 0

		# add carry if necessary
		if carry != 0:
			final = str(carry) + final
	
		return final