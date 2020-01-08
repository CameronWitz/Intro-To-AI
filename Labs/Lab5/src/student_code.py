import common

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount_per_cycle):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	#
	ystart = None
	xstart = None
	
	actions = {}
	# define actions movement and cost (change to y, change to x, multiplier for battery)
	actions[1] = [1, 0, 1, (2, 4)] # south can have east and west...
	actions[2] = [0, -1, 1, (1, 3)] # west can have north and south
	actions[3] = [-1, 0, 1, (2, 4)] # north can have same as south etc...
	actions[4] = [0, 1, 1, (1, 3)] # 
	
	actions[5] = [1, 0, 2, (6, 8)]
        actions[6] = [0, -1, 2, (5, 7)]
        actions[7] = [-1, 0, 2, (6, 8)]
        actions[8] = [0, 1, 2, (5, 7)]
	
	# Initialize base cases...
	for y in range(6):
		for x in range(6):		
			if map[y][x] == common.constants.PIZZA:
				ystart = y
				xstart = x
				
			elif map[y][x] == common.constants.RIVAL:
				values[y][x] = -dronerepair_cost
				policies[y][x] = common.constants.EXIT

			elif map[y][x] == common.constants.CUSTOMER:
				values[y][x] = delivery_fee
                                policies[y][x] = 0

			else:
				values[y][x] = 0
	
	# Begin dynamic program...
	g = 1 - discount_per_cycle
	improvement = 100
	liv_pen = -battery_drop_cost
	while(improvement >= 0.01):
		old_vals = values[:]
		improvement = 0
		for y in range(6):
			for x in range(6):
				if map[y][x] == common.constants.RIVAL:
					pass
				elif map[y][x] == common.constants.CUSTOMER:
					pass
				else:
					choices = []
					for choice in range(1, 9):
                        			tval = 0
                        			data = actions[choice]
                        			ychg = data[0]
                        			xchg = data[1]
                        			mult = data[2]
                        			others = data[3]
                        			p = 0.7 if mult == 1 else 0.8
                        			op = (1-p)/2
						ynew = y + ychg if (y + ychg) < 6 and (y + ychg) >= 0 else y
                        			xnew = x + xchg if (x + xchg) < 6 and (x + xchg) >= 0 else x	
 
						tval += liv_pen*mult + p*g*old_vals[ynew][xnew]

						for ochoice in others:
                                			ychg = actions[ochoice][0]
                                			xchg = actions[ochoice][1]
                               				ynew = y + ychg if (y + ychg) < 6 and (y + ychg) >= 0 else y
                                			xnew = x + xchg if (x + xchg) < 6 and (x + xchg) >= 0 else x						
							tval += op*g*old_vals[ynew][xnew]
						print(tval)
						choices.append((tval, choice))
			
					choices = sorted(choices, key = lambda x: x[0], reverse = True)
					best_val, best_choice = choices[0]
					improvement += abs(values[y][x] - best_val)
					values[y][x] = best_val
					policies[y][x] = best_choice 
	
	return values[ystart][xstart]








