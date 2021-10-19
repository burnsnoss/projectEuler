''' 
project euler problem 19 - burnsnoss - 10/18/2021
number of sundays on the first of the month in the 20th century
'''

import time

# class Date():

# 	year = 0
# 	month = ''
# 	day = 0

# 	def __init__(self, y, m, d):
# 		self.year = y
# 		self.month = m
# 		self.day = d
# 		return


months = {
	'jan': 31,
	'feb': 28,
	'mar': 31,
	'apr': 30,
	'may': 31,
	'jun': 30,
	'jul': 31,
	'aug': 31,
	'sep': 30,
	'oct': 31,
	'nov': 30,
	'dec': 31
}



if __name__ == '__main__':
	tic = time.clock()

	year = 1901
	sundays = 0
	# jan 1 1901 is a Tuesday
	offset = 2
	while year <= 2000:
		for m in months.keys():

			# check if its a leap year/feb
			if (year % 4) == 0 and m == 'feb':
				offset += 1

			if not (year == 2000 and m == 'dec'):
				offset += months[m]
			
			if offset % 7 == 0:
				# this is a sunday
				sundays += 1

		year += 1

	print(sundays)



	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()