# project euler problem 1
# find all multiples of 3 and 5 below 1000 and add them together

if __name__ == '__main__':
	# init total variable
	total = 0
	# find multiples of 3 and add them to total
	multiple = 3
	while multiple < 1000:
		total += multiple
		multiple += 3
	# do the same for multiples of 5, 
	# but also check if its a multiple of 3
	# dont add the repeated multiples
	multiple = 5
	while multiple < 1000:
		if multiple % 3 != 0:
			total += multiple
		multiple += 5

	print(total)
	exit()