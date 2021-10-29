''' 
project euler problem 25 - burnsnoss - 10/21/2021
thousand-digit fibonnaci number
'''

import time
from util import sigma



if __name__ == '__main__':
	tic = time.clock()

	# count up to a 1000 digit number using my cool sigma adding machine

	idx = 2
	f1 = '1'
	f2 = '1'

	while True:
		idx += 1
		f3 = sigma([f1, f2])
		if len(f3) >= 1000:
			break
		f1 = f2
		f2 = f3

	print(f3)
	print(idx)


	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()