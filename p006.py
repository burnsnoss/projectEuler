''' 
project euler problem 6 - burnsnoss - 9/1/2021

find the difference between the "sum of squares" and the 
 "square of sums" of the first 100 natural numbers
'''



if __name__ == '__main__':
	sum_of_squares = 0 
	square_of_sum = 0

	# iterate from 1 to 100, get the sums and squares and such
	for i in range(1, 101):
		sum_of_squares += i**2
		square_of_sum += i

	square_of_sum = square_of_sum**2

	difference = square_of_sum - sum_of_squares

	print(difference)

	exit()


