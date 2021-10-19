# project euler problem 2
# find sum of all fibonacci numbers below 4 million

upper_limit = 4000000

if __name__ == '__main__':
	# generate fibonacci numbers and sum the ones that are even
	previous = 1
	current = 2
	total = 0
	while current <= upper_limit:
		if current % 2 == 0:
			# current number is even, add it to total
			total += current 
		# calculate next fib number
		next_fib_num = previous + current
		# set new previous and current
		previous = current
		current = next_fib_num

	print(total)
	
	exit()