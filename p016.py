''' 
project euler problem 16 - burnsnoss - 10/7/2021
big binomial number conversion
'''

import time
from util import sigma



if __name__ == '__main__':
	tic = time.clock()
	
	# 2^15 = 32768
	# what are the sum of the digits of 2^1000?

	# going to use doubling method and a string adder from p013
	# to get number in base 10
	c = '1'
	for i in range(1000):
		c = sigma([c, c])

	# add up digits
	total = 0
	for n in c:
		total += int(n)

	print(total)

	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()