# Function that evaluates a given board and returns a value based on the configuration of the neural network
import random #For random generation functions
import itertools #For sweet fast list functions

# A representation of a checker board
class board():
	location = [] # There are 32 spots on a checker board, each spot is either e, r, b, R, B (empty, red, black, red king, black king)

	def randomBoard(self): #Generates a random board, NOTE: Will not be a valid board, just one with random stuff on it
		choices = ['e', 'r', 'b', 'R', 'B']
		for x in xrange(32):
			self.location.append(random.choice(choices))

class neuralNode(): # A node consists of some weights by which it listens to the previous layer
	weights = []

	def __init__(self, number): #Generates a node with random weights to a number of previous nodes

		for link in range(number):
			self.weights.append(random.uniform(-1,1))

	def evaluateLayer(self, layer): #Returns how much this node likes the input layer
		for piece in itertools.izip(self.weights, layer):
			likeness += piece[0] + piece[1]
		return likeness


# Contains a neural network, which consists of multiple layers, each layer consists of multiple nodes each one connected to each node from the previous layer
class neuralNetwork(object):
	neuralNodes = []

	def evaluateBoard(self, board): #Evaluates a board and returns how much the neural network likes it
		result = []
		result.append([])
		# First the input nodes
		for node, location in zip(self.neuralNodes[0], board):
			result[0].append(node.weights[0]*location)

		# Next the rest of the nodes
# This is the complex part, we need to step through each node in each layer and multiply each of it's weights by the nodes results in the previous layer
		for x,y in zip(self.neuralNetwork[1:], range(self.neuralNodes)): # Each layer
			result.append()
			for node in x: # Each node
				result[y+1].append(evaluateLayer(result[y]))
		return [x for x in result[-1:]][0]
		#return returnResult #We assume that the last element of the array only has one value

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
# For the first group
		self.neuralNodes.append([])
		for x in range(layersInfo[0]):
			self.neuralNodes[0].append(neuralNode(1))

# Now for the rest
		def addLayer(curLayer, prevLayer):
			result = []
			for node in range(curLayer):
				result.append(neuralNode(prevLayer))
			return result

		for layer in itertools.starmap(addLayer, zip(layersInfo[1:], layersInfo)):
			self.neuralNodes.append(layer)

if __name__ == "__main__":
	pass
