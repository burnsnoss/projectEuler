''' 
project euler problem 20 - burnsnoss - 10/19/2021
big factorial digit sum
'''

# method here will just be to use my sigma adder to 'multiply'
# ie 100 x 99 = 100 + 100 + 100 ... (99 times) and so on

import time
from util import sigma



if __name__ == '__main__':
	tic = time.clock()
	
	n = 100

	total = n 

	for i in range(n, 1, -1):
		# generate a list of numbers to add using sigma
		add_list = [str(total) for x in range(i-1)]
		total = sigma(add_list)

	print(total)

	digit_sum = 0
	for digit in total:
		digit_sum += int(digit)

	print(digit_sum)
	
	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()