import common
def astar_search(map_):
    MAP_WIDTH = common.constants.MAP_WIDTH
    MAP_HEIGHT = common.constants.MAP_HEIGHT
    
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
    
    start_found = False
    start_y = None
    start_x = None
    
    goal_found = False
    goal_y = False
    goal_x = False
    
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if map_[y][x] == startval:
                start_found = True
                start_y = y
                start_x = x
            
            if map_[y][x] == goal:
                goal_found = True
                goal_x = x
                goal_y = y
        # Exit outer loop if we have found both start and end        
        if start_found and goal_found:
            break
            
    if not start_found or not goal_found:
        return found

    # Otherwise begin the A* search
    n = MAP_HEIGHT
    startpos = (start_y, start_x)
    parents = {}
    parents[(y, x)] = startpos # parents stores the parent position, and number of steps to parent
    # in our queue, we will store the position, and the number of steps taken to get to this node. 
    queue.append([startpos, 0])
    stops = [visited, wall]

    while(queue != []):
        # At this point queue should be sorted according to the A* heuristic
        pos, steps = queue.pop(0)
        x = pos[1]
        y = pos[0]

        val = map_[y][x]

        if val == goal:
            found = True
            map_[y][x] = 5
            break
        
        if val not in stops: 
            map_[y][x] = visited
            
            # Check which nodes to add to queue 
            if x+1 < MAP_WIDTH:
                tval = map_[y][x+1]
                if tval not in stops:
                    pos = [(y, x+1), steps+1]
                    
                    queue.append(pos)
                    parents[(y, x+1)] = (y,x)


            if y +1 < MAP_HEIGHT:
                tval = map_[y+1][x]  
                if tval not in stops:  
                    pos = [(y+1, x), steps+1]
                    
                    queue.append(pos)
                    parents[(y+1, x)] = (y,x)


            if x-1 >= 0:
                tval = map_[y][x-1]
                if tval not in stops:
                    pos = [(y, x-1), steps+1]
                    
                    queue.append(pos)
                    parents[(y, x-1)] = (y,x)


            if y -1 >= 0:
                tval = map_[y-1][x]
                if tval not in stops:
                    pos = [(y-1, x), steps+1]
                    
                    queue.append(pos)
                    parents[(y-1, x)] = (y,x)
        
        # Re-sort the queue according to the A* heuristic
        queue = sorted(queue, key = lambda x: (x[1] + abs(x[0][0] - goal_y) + abs(x[0][1] - goal_x), x[0][1], x[0][0]))

    if found:
        while(pos != startpos):
            y = pos[0]
            x = pos[1]
            map_[y][x] = 5
            pos = parents[(y, x)]
        y = pos[0]
        x = pos[1]
        map_[y][x] = 5


    return found
   
