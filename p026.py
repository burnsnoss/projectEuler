''' 
project euler problem 26 - burnsnoss - 10/21/2021

'''

import time
from util import divider



if __name__ == '__main__':
	tic = time.clock()

	n = 1000

	max_rpt = 0
	d = 0

	# iterate through numbers less than 1000
	for i in range(2, n):
		# get the quotient of dividing these numbers by one
		q, rpt = divider(1, i)

		# check length of the repeating section if there is one
		if len(rpt) > max_rpt:
			# keep track of which number has longest repeating section
			max_rpt = len(rpt)
			d = i

	print(d, max_rpt)



	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()