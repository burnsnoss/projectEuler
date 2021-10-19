''' 
project euler problem 15 - burnsnoss - 10/6/2021
lattice paths through grid
'''

# https://www.xarg.org/puzzle/project-euler/problem-15/
# ^ dynamic programming solution here that is also cool

import time

def findPaths(s, x, y):
	# this is ridiculously slow 
	# apparently there is a dynamic programming solution
	# print(s, x, y)
	if x == s and y == s:
		return 1
	if x == s and y != s:
		return findPaths(s, x, y+1)
	elif x != s and y == s:
		return findPaths(s, x+1, y)
	else:
		return findPaths(s, x+1, y) + findPaths(s, x, y+1)


def dynamicPaths(n):
	# dynamic programming solution
	# generates a symmetrical matrix of pascals triangle numbers
	# our solution will be at grid[n][n]
	grid = [[0 for x in range(n+1)] for x in range(n+1)]

	grid[0][0] = 1

	for i in range(0, n+1):
		for j in range(0, n+1):
			if i > 0:
				grid[i][j] += grid[i-1][j]
			if j > 0:
				grid[i][j] += grid[i][j-1]

	return grid[n][n]




# found a solution online looks like its something about binomial coefficients?
def fastPath(n):
	c = 1
	for i in range(1, n+1):
		c = c * (n + i) / i
	return c

	


if __name__ == '__main__':
	tic = time.clock()
	# not gonna lie i have no idea how to do this
	s = 20        # side length of grid
	x, y = 0, 0   # starting point

	# paths = findPaths(s, x, y)
	paths = dynamicPaths(s)
	# paths = fastPath(s)

	print(paths)
	
	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()