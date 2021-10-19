# project euler problem 5
# smallest positive number evenly divisible by all of the numbers from 1 to 20
'''NOTE: apparently a solution exists where you just find the prime factorization
    of numbers from 1-20, and then take the highest power of each prime factor found
    and multiply those together. idk how this works. my solutions works in a second 
    or two which isnt exactly fast, but...''' 

def checkFactorization(a, b, n):
	# returns true if the numbers in the range [a, b] are factors of n
	# else false
	i = a
	while i <= b:
		if n % i != 0:
			return False

		i += 1

	return True



if __name__ == '__main__':
	# TACTICAL BUT BRUTISH TACTIC: 
	# take multiples of 20 and check those for divisibility

	# we know up to 2519 doesnt work, so start with the closest multiple of 20
	x = 2520

	while True:
		if checkFactorization(1, 20, x):
			print(x)
			exit()

		x += 20

	exit()


