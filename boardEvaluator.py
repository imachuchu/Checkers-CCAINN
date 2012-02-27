# Function that evaluates a given board and returns a value based on the configuration of the neural network
import random #For random generation functions

# A representation of a checker board
class board():
	location = [] # There are 32 spots on a checker board, each spot is either e, r, b, R, B (empty, red, black, red king, black king)

	def randomBoard(self): #Generates a random board, NOTE: Will not be a valid board, just one with random stuff on it
		choices = ['e', 'r', 'b', 'R', 'B']
		for x in xrange(32):
			self.location.append(random.choice(choices))

class neuralNode():
	weights = []
	def evaluateNode():
		

# Contains a neural network, which consists of multiple layers, each layer consists of multiple nodes each one connected to each node from the previous layer
class neuralNetwork(object):
	weights = []

	def evaluateBoard(self, board): #Evaluates a board and returns how much the neural network likes it
		# First the input nodes
		previous = map(lambda x,y: x*self.getValue(y), self.weights[0], board.location)
		# Next the rest of the nodes

# This is the complex part, we need to step through each node in each layer and multiply each of it's weights by the nodes results in the previous layer
		output = previous
		previousLayer = output.__iter__()
		resultAr = []
		for layer in self.weights[1:]:
			for node in layer:
				zipAr = zip(node, previousLayer)
				resultAr.append(sum(sum(zipAr)))
			output.append(resultAr)
			resultAr = []
			previousLayer.next()

	def getValue(self, piece): # Simple call that returns the value of each piece, based on our color. NOTE: currently we hard code red
		if piece == 'r':
			return float(1)
		if piece == 'b':
			return float(-1)
		if piece == 'R':
			return float(1.4)
		if piece == 'B':
			return float(-1.4)
		return 0


# Example usage: randomNetwork([32,40,10,1])
	def randomNetwork(self, layersInfo): #Generates a random network, given an array of node distribution
		self.weights.append([])
		for x in range(layersInfo[0]):
			self.weights[0].append(random.uniform(-1,1))
		for layer in layersInfo[1:]:
			array = map(lambda x: map(lambda x: random.uniform(-1,1), range(len(self.weights[-1]))), range(layer))
			self.weights.append(array)

if __name__ == "__main__":
	pass
