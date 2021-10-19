''' 
project euler problem 11 - burnsnoss - 9/4/2021
greatest directional product in grid
'''

import time

def getGreatestProduct(grid, x, y):
	# returns the greatest product counting four spaces
	# out from coordinate x, y in eight directions
	directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
	greatest = 1
	for d in directions:
		product = 1
		if d == 'n':
			for i in range(4):
				if x-i < 0:
					break
				product *= grid[x-i][y]

		elif d == 'ne':
			for i in range(4):
				if x-i < 0 or y+i >= len(grid[x]):
					break
				product *= grid[x-i][y+i]

		elif d == 'e':
			for i in range(4):
				if y+i >= len(grid[x]):
					break
				product *= grid[x][y+i]

		elif d == 'se':
			for i in range(4):
				if x+i >= len(grid) or y+i >= len(grid[x]):
					break
				product *= grid[x+i][y+i]

		elif d == 's':
			for i in range(4):
				if x+i >= len(grid):
					break
				product *= grid[x+i][y]

		elif d == 'sw':
			for i in range(4):
				if x+i >= len(grid) or y-i < 0:
					break
				product *= grid[x+i][y-i]

		elif d == 'w':
			for i in range(4):
				if y-i < 0:
					break
				product *= grid[x][y-i]

		elif d == 'nw':
			for i in range(4):
				if x-i < 0 or y-i < 0:
					break
				product *= grid[x-i][y-i]

		if product > greatest:
			greatest = product

	return greatest




if __name__ == '__main__':
	tic = time.clock()

	fs = open('p011_input.txt', 'r')

	grid = []
	for line in fs:
		l = line.strip('\n')
		l = l.split(' ')
		grid.append(list(map(int, l)))

	greatest = 0
	for x in range(len(grid)):
		for y in range(len(grid[x])):
			product = getGreatestProduct(grid, x, y)
			if product > greatest:
				greatest = product

	print(greatest)

	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()