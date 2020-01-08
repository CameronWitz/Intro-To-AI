import common

# Define a win for X to be 1 and a win for O to be -1
xwin = 1
owin = -1
tie = 0 #... and a tie to be 0

def maxval(board, turn):
	val = -2 # has to be less than owin
	# check whose turn it is...
	next_ = common.constants.O if turn == common.constants.X else common.constants.O
	# Check if the game is already finished or not...
	gstat = common.game_status(board)
	if gstat == common.constants.O:
		val = -1
	elif gstat == common.constants.X:
		val = 1
	elif common.constants.NONE not in board:
		val = 0
	else:
		for i in range(3):
			for j in range(3):
				cval = common.get_cell(board, i, j)
				if cval == common.constants.NONE:
					newboard = board[:]
					common.set_cell(newboard, i, j, turn)
					val = max(val, minval(newboard, next_))
	return val
					


def minval(board, turn):
        val = 2 # has to be less than owin
        # check whose turn it is...
	if turn == common.constants.O:
		next_ = common.constants.X
	else:
		next_ = common.constants.O
        
        # Check if the game is already finished or not...
        gstat = common.game_status(board)
        if gstat == common.constants.O:
                val =  -1
        elif gstat == common.constants.X:
                val =  1
	elif common.constants.NONE not in board:
		val = 0
        else:	
                for i in range(3):
                        for j in range(3):
                                cval = common.get_cell(board, i, j)
                                if cval == common.constants.NONE:
                                        newboard = board[:]
                                        common.set_cell(newboard, i, j, turn)
                                        val = min(val, maxval(newboard, next_))
        return val

def minmax_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	res = 0
	if turn == common.constants.O:
		res = minval(board, turn)
	else: # it's X's turn
		res = maxval(board, turn)
	
	if res == 1:
		return common.constants.X
	elif res == -1:
		return common.constants.O
	else: 
		return common.constants.NONE
#######
# ab helper funcs

def abminval(board, turn, a, b):
        val = 2 # has to be less than owin
        # check whose turn it is...
	if turn == common.constants.O:
		next_ = common.constants.X
	else:
		next_ = common.constants.O
        
        # Check if the game is already finished or not...
        gstat = common.game_status(board)
        if gstat == common.constants.O:
                val =  -1
        elif gstat == common.constants.X:
                val =  1
	elif common.constants.NONE not in board:
		val = 0
        else:
                for i in range(3):
                        for j in range(3):
                                cval = common.get_cell(board, i, j)
                                if cval == common.constants.NONE:
                                        newboard = board[:]
                                        common.set_cell(newboard, i, j, turn)
                                        val = min(val, abmaxval(newboard, next_, a, b))
					if val <= a:
						return val
					b = min(val, b) 
        return val


def abmaxval(board, turn, a, b):
	val = -2 # has to be less than owin
	# check whose turn it is...
	next_ = common.constants.O if turn == common.constants.X else common.constants.O
	# Check if the game is already finished or not... 
	gstat = common.game_status(board)
	if gstat == common.constants.O:
		val = -1
	elif gstat == common.constants.X:
		val = 1
	elif common.constants.NONE not in board:
		val = 0
	else:
		for i in range(3):
			for j in range(3):
				cval = common.get_cell(board, i, j)
				if cval == common.constants.NONE:
					newboard = board[:]
					common.set_cell(newboard, i, j, turn)
					val = max(val, abminval(newboard, next_, a, b))
					if val >= b:
						return val
					a = max(val, a)
	return val
	

def abprun_tictactoe(board, turn):
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);
	res = 0
        if turn == common.constants.O:
                res = abminval(board, turn, -1, 1)
        else: # it's X's turn
                res = abmaxval(board, turn, -1, 1)
        if res == 1:
                return common.constants.X
        elif res == -1:
                return common.constants.O
        else:
                return common.constants.NONE
