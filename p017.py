''' 
project euler problem 17 - burnsnoss - 10/7/2021
number to english counter
'''

import time

def lessThanTwenty(n):
	names = [ 'zero', 'one', 'two', 'three', 'four', 'five',
		'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
		'twelve', 'thirteen', 'fourteen', 'fifteen', 
		'sixteen', 'seventeen', 'eighteen', 'nineteen']
	return names[int(n)]


def twentyToOneHundred(n):
	names = ['zero', 'ten', 'twenty', 'thirty', 'forty',
		'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	if n[-1] == '0':
		return names[int(n[0])]
	else:
		return names[int(n[0])] + lessThanTwenty(n[-1])


def oneHundredToOneThousand(n):
	if n[-2:] == '00':
		return lessThanTwenty(n[0]) + 'hundred'
	elif int(n[-2:]) < 20:
		return lessThanTwenty(n[0]) + 'hundredand' + lessThanTwenty(n[-2:])
	else:
		return lessThanTwenty(n[0]) + 'hundredand' + twentyToOneHundred(n[-2:])

def intToEnglish(n):
	if int(n) < 20:
		return lessThanTwenty(n)
	elif int(n) >= 20 and int(n) < 100:
		return twentyToOneHundred(n)
	elif int(n) >= 100 and int(n) < 1000:
		return oneHundredToOneThousand(n)
	else:
		return 'onethousand'


if __name__ == '__main__':
	tic = time.clock()
	
	total = 0
	for i in range(1, 1001):
		total += len(intToEnglish(str(i)))
		print(intToEnglish(str(i)))

	print(total)
	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()