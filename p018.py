''' 
project euler problem 18 - burnsnoss - 10/18/2021
max path sum in integer triangle
'''

import time

# class Node():

# 	value = None
# 	parent = None
# 	left = None
# 	right = None

# 	def __init__(self, value):

# class BinaryTree():

# 	nodes = []

# 	def __init__(self):


class Triangle():

	triangle = []

	def __init__(self):
		return 

	# adds a row to the triangle (read from input file)
	def addRow(self, row):
		self.triangle.append(row)
		return

	# print the triangle so we can visualize it
	def printTriangle(self):
		for row in self.triangle:
			print(row)
		# print(self.triangle[x][y])
		return

	# start from the bottom, calculate the max of each 2-child 1-parent sum
	# store that sum over the parent, and repeat until you hit the root
	def maxPath(self):
		row_idx = len(self.triangle) - 1

		# for each row, until we hit the 0th row
		while row_idx > 0:
			# for each element in the row, up to the second to last element
			for i in range(len(self.triangle[row_idx]) - 1):
				# compare two child nodes with each other, and 
				# replace the parent node with the max sum 

				# max_value is the max of the children nodes
				max_value = max(int(self.triangle[row_idx][i]), int(self.triangle[row_idx][i+1]))

				# replacing the parent with the max_value + parent sum
				self.triangle[row_idx-1][i] = max_value + int(self.triangle[row_idx-1][i])

			row_idx -= 1

		return self.triangle[0][0]




if __name__ == '__main__':
	tic = time.clock()
	
	# initialize an empty triangle
	t = Triangle()

	# iterating over lines in our input file
	fs = open('p018_input.txt', 'r')
	for line in fs:
		line = line.strip('\n')
		line = line.split(' ')
		# add each row to our triangle class instance
		t.addRow(line)

	max_path = t.maxPath()

	print(max_path)


	toc = time.clock()
	print(f'time: {(toc - tic):.4f}s')
	exit()