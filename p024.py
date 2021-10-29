''' 
project euler problem 24 - burnsnoss - 10/21/2021
millionth lexicographical permutation of 10 digits
'''

import time
from util import factorial


if __name__ == '__main__':
	tic = time.clock()

	# do n! to find total number of permutations
	# divide by n
	# find the range where the millionth permutation will be
	#  (since we are ordered lexicographically)
	# do this recursively to find the range within the other permutations

	# generate permutation numbers
	n = 10
	numbers = []
	for x in range(0, n):
		numbers.append(x)

	t = 999999
	#print('t', t)

	# every loop, calculate permutation range where the solution will be
	# pop the number off that those permutations will begin with,
	# add that number to another list,
	# then run it again
	final_permutation = []
	while len(numbers) > 1:
		# n! / n gives you interval size
		interval_size = factorial(len(numbers))//(len(numbers))
		#print('interval size', interval_size)

		# number of intervals until we hit the millionth number
		num_intervals = t // interval_size
		#print('num intervals', num_intervals)

		final_permutation.append(numbers.pop(num_intervals))
		#print('poplist', final_permutation)
		#print('oglist', numbers)

		t -= (num_intervals * interval_size)
		if t == 0:
			while len(numbers) > 1:
				final_permutation.append(numbers.pop(0))
			break
		#print('t', t)

	final_permutation.append(numbers.pop())
	#print(final_permutation)
	final_answer = ''
	for p in final_permutation:
		final_answer += str(p)

	print(final_answer)

		
	
	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()