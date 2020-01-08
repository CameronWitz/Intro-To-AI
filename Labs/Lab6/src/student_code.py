import common

class bin_perceptron:
	def __init__(self, dim, data_train, data_test):
		self.W = [0]*(dim+1)
		self.train = data_train
		self.test = data_test
	
	def dot(self, data):
		res = self.W[0]*data[0] + self.W[1]*data[1] + self.W[2]
		return res 

	def update(self, data):
		lab = data[2]
		tlab = 1 if self.dot(data) >= 0 else 0
		if tlab == lab:
			return 1 # for correct
		else: #tlab != lab
			if lab == 0:
				chg = -1.
			else:
				chg = 1.
			self.W = [self.W[0] + chg*data[0],
				  self.W[1] + chg*data[1],
				  self.W[2] + chg] 	
			return 0 #for wrong

	def predict(self, data):
		tlab = 1 if self.dot(data) >= 0 else 0
		return tlab

	def make_preds(self):
		for row in self.test:
			pred = self.predict(row)
			row[2] = pred
		return self.test

	def Train(self):
		total = float(len(self.train)) 
		for row in self.train:
			self.update(row)
		correct = 0.
		for row in self.train:
			v = self.dot(row)
			lab = row[2]
			tlab = 1 if v >= 0 else 0
			correct += 1. if tlab == lab else 0.
		return correct/total
class  multi_perceptron:
	
	def __init__(self, targets, train, test):
		self.targets = targets
		self.train = train
		self.test = test
		self.Ws = [[0]*3 for i in targets]
	def argmax(self, vals):
		mval = vals[0]
		maxdex = 0
		for i, v in enumerate(vals):
			if v >= mval:
				mval = v
				maxdex = i
		return maxdex

	def dot(self, data):
		vals = []
		for W in self.Ws:
			temp = W[0]*data[0] + W[1]*data[1] + W[2]
			vals.append(temp)
		return vals
	
	def update(self, data):
		vals = self.dot(data)
		tlab = self.argmax(vals)
		lab = int(data[2])
		
		if tlab == lab:
			#nochange
			return 1
		else:
		
			self.Ws[lab][0] = self.Ws[lab][0] + data[0] 
			self.Ws[lab][1] = self.Ws[lab][1] + data[1]
			self.Ws[lab][2] += 1

			self.Ws[tlab][0] = self.Ws[tlab][0] - data[0]
                        self.Ws[tlab][1] = self.Ws[tlab][1] - data[1]
                        self.Ws[tlab][2] -= 1			

			return 0
	
	def Train(self):
		total = float(len(self.train))
		for row in self.train:
			self.update(row)
		data = self.train[:]
		correct = 0.
		for row in self.train:
			lab = row[2]
			vals = self.dot(row)
			tlab = self.argmax(vals)
			correct += 1. if tlab == lab else 0. 
		return correct/total
	def predict(self):
		for row in self.test:
			vals = self.dot(row)
			lab = self.argmax(vals)
			row[2] = lab

		return self.test



def part_one_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1
	perceptron = bin_perceptron(common.constants.DATA_DIM, data_train[:], data_test[:])
	acc = 0
	iteration = 0
	while acc < 1:
		acc = perceptron.Train()
	#	print iteration, acc
		iteration += 1
	data_test = perceptron.make_preds()
	return

def part_two_classifier(data_train,data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8
	perceptron = multi_perceptron([i for i in range(9)], data_train, data_test)
	acc = 0
	iteration = 0
	while acc <= 0.95:# and iteration <= 100:
		acc = perceptron.Train()
	#	print iteration, acc
		iteration += 1
	data_test = perceptron.predict()
	return
