'''
utility class for project euler problems
''' 

def getFactors(n, perfect = False):
	# returns a list of factors of n
	# if it returns just [1, n], then it's prime
	# should probably write another function that would take less time
	#  to determine just if a number is prime, like isPrime()
	# pass in perfect = True to return just perfect divisors of n
	if n == 0:
		return [0]

	i = 2
	fs = [1]           # factors lists
	fs2 = [n]
	target = n
	sqrt = n ** 0.5    # makes it slightly faster if number is prime
	while i < target and i <= sqrt:
		if n % i == 0:
			fs.append(i)
			target = n // i
			# if perfect factors, don't add square roots 
			if target != i or not perfect:
				fs2.insert(0, target)

		i += 1

	# remove n if perfect factors only
	if perfect:
		fs2.pop(-1)

	return fs + fs2


def isPrime(n):
	''' uses getFactors to determine if number is prime, 
	      returns True if it is and False if not '''
	if n < 0:
		return False
	if len(getFactors(n)) <= 2:
		return True 
	return False



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
# can handle big numbers 
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


# factorial function, works on big numbers
def factorial(n):
	if int(n) <= 10:
		return recursiveFactorial(n)

	total = n
	for i in range(n, 1, -1):
		# generate a list of numbers to add using sigma
		add_list = [str(total) for x in range(i-1)]
		total = sigma(add_list)

	return total


# EZ clap factorial function for small numbers
def recursiveFactorial(n):
	if n == 1:
		return n
	else:
		return n * recursiveFactorial(n-1)



def fibonacci(n):
	''' returns the nth fibonacci number; assuming f(1) = f(2) = 1 '''
	if n < 3:
		return 1

	idx = 2
	f1 = '1'
	f2 = '1'

	while True:
		idx += 1
		f3 = sigma([f1, f2])
		if idx == n:
			break
		f1 = f2
		f2 = f3

	return f3



def divider(d1, d2):
	''' pass in two INTEGERS that you would like divided 
	     it will divide until it resolves or repeats.
	     it basically performs long division.
	     d1 = dividend
	     d2 = divisor
	      returns:
	        the quotient 
	        the repeating portion of the decimal (will be 0 if resolved) '''

	if int(d1) > int(d2):
		return greaterThanOneDivide(d1, d2)
	elif int(d1) == int(d2):
		return '1', '0'

	# the answer here will be less than one

	# add the first dividend to the list here
	dividends = [str(d1)]

	# since d2 > d1, add a zero off the bat, add that number to the dividends list
	d1 = str(d1) + '0'
	dividends.append(d1)

	# keep track of dividends index?
	idx = 1

	# answer is less than one, so start quotient this way
	quotient = '0.'

	resolved = False

	while True:
		 multiplier = int(d1) // int(d2)
		 quotient += str(multiplier)
		 remainder = int(d1) % int(d2)

		 if remainder == 0:
		 	# we've resolved
		 	resolved = True
		 	break

		 # if there is a remainder, then add a zero to it
		 #  set it equal to d1
		 d1 = str(remainder) + '0'

		 # check if d1 is in dividends, add if it is not
		 # if it is, break, and return the repeating segment
		 try:
		 	idx = dividends.index(d1)
		 	break
		 except ValueError:
		 	dividends.append(d1)
		 	continue




	if resolved:
		return quotient, '0'
	else:
		return quotient, quotient[idx+1:]



def greaterThanOneDivide(d1, d2):
	pass