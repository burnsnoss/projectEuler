''' 
project euler problem 14 - burnsnoss - 9/15/2021
Collatz sequence
'''

import time



if __name__ == '__main__':
	tic = time.clock()

	# basic idea is to keep a big matrix of collatz sequences
	# index of each row is starting number
	# faster method (maybe): as soon as you get ANY number you've seen before
	# slap that numbers' sequence down

	biggest = []
	sequences = []
	sequences.append([0])
	ceiling = 1000000

	for i in range(1, ceiling + 1):

		# sequences[i] = [i]
		sequences.append([i])
		n = i

		while True:
			if n % 2 == 0:
				n = int(n / 2)
			else:
				n = int((3 * n) + 1)

			sequences[i] += [n]

			if n == 1:
				break

			# was using this for sequences dict but is slower than list ):
			# if n < i or (n < ceiling + 1 and n in sequences.keys()):
			# 	sequences[i] = sequences[i] + sequences[n][1:]
			# 	break

			if n < i:
				sequences[i] = sequences[i] + sequences[n][1:]
				break


		if len(sequences[i]) > len(biggest):
			biggest = sequences[i]


	print(biggest)

	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()