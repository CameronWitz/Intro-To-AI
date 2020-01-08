import common
import math

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	
	bmin = -1000
	bmax = 1000
	mmin = -10
	mmax = 10
	#line_space = {}
	space = common.init_space(2000, 2000)
	bestm = 0
	bestb = 0
	maxval = 0
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			r = image[0][y][x]
			g = image[1][y][x]
			b = image[2][y][x]
			if r == 0 and g == 0 and b == 0: # black pixel
				# find feasible lines
				#b = y - m*x
				for m in range(2000):
					mval = (m-1000)*0.01
					b = y - mval*x
					if b >= bmin and b <= bmax:
						b = int(b)
						space[m][b] += 1
						if space[m][b] >= maxval:
							bestb = b
							bestm = mval
							maxval = space[m][b]
	# find the highest voted line
	line.m = bestm
	line.b = bestb
	return line
	

def detect_normal(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.theta and line.r
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	line=common.Line()
	
	space = common.init_space(1800, 1800)
	
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			r = image[0][y][x]
			g = image[1][y][x]
			b = image[2][y][x]
			if r == 0 and g == 0 and b == 0: # black pixel
				for deg in range(1800):
					R  = x*math.cos(deg*math.pi/1800) + y * math.sin(deg*math.pi/1800)
					if R <= 900 and R >= -900:
						R = int(R) + 900
						space[R][deg] += 1
	bestR = 0
	bestdeg = 0
	maxval = 0
	for deg in range(1800):
		for R in range(1800):
			val = space[R][deg]
			if val >= maxval:
				maxval = val
				bestdeg = deg
				bestR = R
	line.r= bestR - 900
	line.theta= (bestdeg*math.pi/1800)
	return line

def sobel_x(img, y, x):
	val = 0
	val = val + img[0][y-1][x-1] + 2*img[0][y][x-1] + img[0][y+1][x-1]
	val = val - img[0][y-1][x+1] - 2*img[0][y][x+1] - img[0][y+1][x+1]
	return val
def sobel_y(img, y, x):
	val = 0
	val = val + img[0][y-1][x-1] + 2*img[0][y-1][x] + img[0][y-1][x+1]
	val = val - img[0][y+1][x-1]  - 2*img[0][y+1][x] - img[0][y+1][x+1]
	return val

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[chanel][y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	
	#Sobel edge detection...
	edge_img = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)
	for y in range(1, common.constants.HEIGHT -1):
		for x in range(1, common.constants.WIDTH -1):
			edge_img[y][x] = abs(sobel_x(image, y, x)) + abs(sobel_y(image, y, x))
	space = common.init_space(common.constants.HEIGHT, common.constants.WIDTH)
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			val = edge_img[y][x]
			if val !=  0:
				for yc in range(y-30, y + 31):
					for xc in range(x - 30, x + 31):
						if xc < common.constants.WIDTH and xc >= 0 and yc < common.constants.HEIGHT and yc >= 0:
							rad = (y - yc)**2 + (x - xc)**2
							if rad <= 908 and rad >= 892:
								space[yc][xc] += 1
	maxval = 0
	count = 0
	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			val = space[y][x]
			if val > maxval:
				count = 1
				maxval = val
			elif val == maxval:
				count += 1

	return count







				
