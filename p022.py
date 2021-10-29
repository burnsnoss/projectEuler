''' 
project euler problem 22 - burnsnoss - 10/19/2021
alphabetizing and name scores 
'''

import time
import string

if __name__ == '__main__':
	tic = time.clock()

	# generate alphabet dictionary with letter keys and letter-index values
	alpha = dict.fromkeys(string.ascii_lowercase, 0)
	idx = 1
	for letter in alpha.keys():
		alpha[letter] = idx
		idx += 1

	# open the file for reading
	fs = open('p022_input.txt', 'r')

	# gonna read in the file, sort it, then calculate, brute force

	name_list = fs.read()
	name_list = name_list.strip('\n')
	name_list = name_list.strip('"')
	name_list = name_list.split('","')
	
	# alphabetize the list
	name_list.sort()

	total = 0 
	idx = 1
	for name in name_list:
		score = 0
		# add up letter index values
		for letter in name:
			score += alpha[letter.lower()] 

		# multiply the sum by the name index and add to total
		score = score * idx
		total += score

		idx += 1

	print(total)

	
	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()