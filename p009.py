''' 
project euler problem 9 - burnsnoss - 9/3/2021
finding pythagorean triplet a, b, c
'''

import time

# a^2 + b^2 = c^2
# a + b + c = 1000

# we already know 3^2 + 4^2 = 5^2

if __name__ == '__main__':
	tic = time.clock()

	finish = False

	# brute force it (with some stop conditions)
	# for a in range(3, 1000):
	# 	for b in range(a+1, 1000):
	# 		for c in range(b+1, 1000):

	# 			if a + b + c > 1000:
	# 				break

	# 			if (a*a + b*b) == c*c and a + b + c == 1000 and a < b and b < c:
	# 				print(a,b,c)
	# 				finish = True
	# 				break

	# 		if finish:
	# 			break

	# 	if finish:
	# 		break

	for a in range(3, 1000):
		for b in range(a+1, 1000):
			c = 1000 - b - a
			if c*c == (a*a + b*b):
				print(a, b, c)
				finish = True
				break

		if finish:
			break


	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()