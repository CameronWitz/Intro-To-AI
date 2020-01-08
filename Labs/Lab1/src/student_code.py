import common
#common.constants.MAP_WITDTH
#common.constants.MAP_HEIGHT

def df_helper(map, y, x):
	empty = 0
	wall = 1
	start = 2
	goal = 3
	visited = 4
	
	val = map[y][x]
	if val == goal:
		map[y][x] = 5
		return True
	elif val == visited:
		return False
	elif val == wall:
		return False
	else:
		found = False
		# mark as visited
		map[y][x] = visited
		# search in the correct order
		if x+1 < common.constants.MAP_WIDTH: 
			found =  df_helper(map, y, x+1) or found
		if y+1 < common.constants.MAP_HEIGHT and not found:
			found =  df_helper(map,y+1,x) or found
		if x-1 >= 0 and not found:
			found = df_helper(map, y, x-1) or found
		if y-1 >= 0 and not found: 
			found = df_helper(map, y-1, x) or found
		
		if found:
			map[y][x] = 5
		
		return found
		
def df_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	# First [y][x+1], then [y+1][x], then [y][x-1], and finally [y-1][x]
	start = False
	for y in range(common.constants.MAP_HEIGHT):
		for x in range(common.constants.MAP_WIDTH):
			if map[y][x] == 2:
				start = True
				break	
		if start:
			break
	if start:
		found = df_helper(map, y, x)

	return found


def bf_search(map):
	found = False;
	empty = 0
	wall = 1
	startval = 2
	goal = 3
	visited = 4
	#parents = [None]*common.constants.MAP_WIDTH*common.constants.MAP_HEIGHT

	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	queue = []
	start = False
	for y in range(common.constants.MAP_HEIGHT):
		for x in range(common.constants.MAP_WIDTH):
			if map[y][x] == startval:
				start = True
				break
		if start:
			break
	if not start:
		return found
	
	# Otherwise begin the breadth first search
	n = common.constants.MAP_HEIGHT
	startpos = (y,x)
	parents = {}
	parents[n*y + x] = startpos
	queue.append((y,x))
	stops = [visited, wall]
 
	while(queue != []):
		pos = queue.pop(0)
		x = pos[1]
		y = pos[0]
		
		val = map[y][x]
		
		if val == goal:
			found = True
			map[y][x] = 5
			break
		elif val in stops:
			pass
		else: 
			map[y][x] = visited
			if x+1 < common.constants.MAP_WIDTH:
				tval = map[y][x+1]
				if tval not in stops:
					pos = (y, x+1)
					queue.append(pos)
					parents[n*y + x+1] = (y,x)


			if y +1 < common.constants.MAP_HEIGHT:
				tval = map[y+1][x]  
				if tval not in stops:  
					pos = (y+1, x)
					queue.append(pos)
					parents[n*(y+1) + x] = (y,x)


			if x-1 >= 0:
				tval = map[y][x-1]
				if tval not in stops:
					pos = (y, x-1)
					queue.append(pos)
					parents[n*y + x-1] = (y,x)

			
			if y -1 >= 0:
				tval = map[y-1][x]
				if tval not in stops:
					pos = (y-1, x)
					queue.append(pos)
					parents[n*(y-1) +x] = (y,x)

		

	if found:	
		while(pos != startpos):
			y = pos[0]
			x = pos[1]
			map[y][x] = 5
			pos = parents[n*y + x]
		y = pos[0]
		x = pos[1]
		map[y][x] = 5


	return found
