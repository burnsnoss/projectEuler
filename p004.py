# project euler problem 4
# largest palindrome made from the product of two 3-digit numbers

def isPalindrome(p):
	# determine if number p is a palindrome

	# convert to string
	n = str(p)

	i = 0
	j = len(n) - 1

	# find a stopping point in the palindrome, where to stop checking
	stopping_point = int(len(n) / 2) - 1

	while i <= stopping_point:
		if n[i] != n[j]:
			return False
		i += 1 
		j -= 1

	return True





if __name__ == '__main__':
	# TACTIC:
	# n = numbers 100 through 999
	# did this in reverse bc i had a different idea at first but 
	# basically find all the palindromes possible and then take the max
	# O(N^2)

	
	x = 999

	palindromes = []

	while x >= 100:
		y = 999
		while y >= 100:
			product = x * y
			if isPalindrome(product):
				palindromes.append(product)
			y -= 1

		x -= 1

	print(max(palindromes))
	exit()

