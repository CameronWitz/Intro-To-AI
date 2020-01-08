import common

class variables:
	counter=0


def finished(sudoku):
	done = True
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				done = False
	return done

def findNext(sudoku):
	found = False
	y = None
	x = None
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				y = i
				x = j
				return y, x
	raise ValueError("Didn't find an empty...")

def recursive_bt(sudoku):
	done = finished(sudoku)
	if done:
		return done
	# otherwise...
	# find the next empty location...
	y, x = findNext(sudoku)
	solved = False
	for nval in range(1, 10):
		variables.counter += 1
		canbe = common.can_yx_be_z(sudoku, y, x, nval)
		if canbe:
			sudoku[y][x] = nval
			solved = recursive_bt(sudoku)
		 	if solved == False:
				# reset the changed val to 0
				sudoku[y][x] = 0
			else:
				return solved # True
	return solved


def recursive_fc(sudoku):
	done = finished(sudoku)
	if done:
		return done
	# otherwise...
	# find the next empty location...
	y, x = findNext(sudoku)
	solved = False
	for nval in range(1, 10):
		canbe = common.can_yx_be_z(sudoku, y, x, nval)
		if canbe:
			variables.counter += 1
			sudoku[y][x] = nval
			solved = recursive_fc(sudoku)
		 	if solved == False:
				# reset the changed val to 0
				sudoku[y][x] = 0
			else:
				return solved # True
	return solved

def sudoku_backtracking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	ans = recursive_bt(sudoku)
	return variables.counter

def sudoku_forwardchecking(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	ans = recursive_fc(sudoku)
	return variables.counter

def mrv_helper(sudoku):
	spot_master = {}
	for y in range(9):
		for x in range(9):
			compat = []
			for val in range(1, 10):
				if common.can_yx_be_z(sudoku, y, x, val) and sudoku[y][x] == 0:
					compat.append(val)
			if compat != []:
				spot_master[y, x] = compat
	
	return spot_master

def recursive_mrv(sudoku):

	# Check if the game is done
	done = finished(sudoku)
        if done:
                return done
	# Find the variable that is the most constrained, and begin there	
	spot_master = mrv_helper(sudoku)
	# find the mrv spot
	mkey = (0, 0)
	mval = 100
	for key, val in spot_master.items():
		n = len(val)
		if n < mval:
			mval = n
			mkey = key
		elif n == mval:
			ym, xm = mkey
			y, x = key
			if y == ym:
				if x < xm: # same row, but x is smaller than xm
					mkey = key
			elif y < ym:
				mkey = key
	if mval == 100:
		return False	

	y,x = mkey
	solved = False
	
        for nval in spot_master[mkey]:
		variables.counter += 1
                sudoku[y][x] = nval
                solved = recursive_mrv(sudoku)
                if solved == False:
                # reset the changed val to 0
			sudoku[y][x] = 0
                else:
                        return solved # True
        return solved


def sudoku_mrv(sudoku):
	# PUT YOUR CODE HERE
	# access the sudoku using "sudoku[y][x]"
	# y between 0 and 9
	# x between 0 and 9
	# function must return the number of permutations performed
	# the use of variables.counter to keep track of the worlds 
	# explored is optional but recommended 
	variables.counter=0
	recursive_mrv(sudoku)
	return variables.counter
