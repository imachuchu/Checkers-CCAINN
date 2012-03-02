# Function that evaluates a given board and returns a value based on the configuration of the neural network
import random #For random generation functions
import itertools #For sweet fast list functions
import math #For the e constant

SCALINGFACTOR = .5 #Used by the evolver to modify the resultant weight distribution

# A representation of a checker board
class board():

	def randomBoard(self): #Generates a random board, NOTE: Will not be a valid board, just one with random stuff on it
		self.location = []
		choices = ['e', 'r', 'b', 'R', 'B']
		for x in xrange(32):
			self.location.append(random.choice(choices))

class neuralNode(): # A node consists of some weights by which it listens to the previous layer

	def __init__(self,number=1, inweights=0): #Generates a node with random weights to a number of previous nodes
		weights = []
		self.weights = []
		if inweights != 0:
			self.weights = inweights 
			return
		for link in range(number):
			self.weights.append(random.uniform(-1,1))

	def evaluateLayer(self, layer): #Returns how much this node likes the input layer
		likeness = 0
		for piece in itertools.izip(self.weights, layer):
			likeness += piece[0] + piece[1]
		return likeness

	def evolveNode(self): # Returns a child note evolved off of this one
		futureWeights = []
		for node in self.weights:
			futureWeights.append(1/(1+math.pow(math.e,(-SCALINGFACTOR*node))))
		return neuralNode(inweights=futureWeights)

# Contains a neural network, which consists of multiple layers, each layer consists of multiple nodes each one connected to each node from the previous layer
class neuralNetwork():

	def __init__(self):
		self.neuralNodes = []

	def evaluateBoard(self, board): #Evaluates a board and returns how much the neural network likes it
		result = []
		result.append([])
		# First the input nodes
		for node, location in zip(self.neuralNodes[0], board.location):
			result[0].append(node.weights[0]*self.getValue(location))

		# Next the rest of the nodes
# This is the complex part, we need to step through each node in each layer and multiply each of it's weights by the nodes results in the previous layer
		for x,y in zip(self.neuralNodes[1:], range(len(self.neuralNodes))): # Each layer
			result.append([])
			for node in x: # Each node
				result[y+1].append(node.evaluateLayer(result[y]))
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

	def evolveNetworks(self, number): #Function to return evolved networks, returns an array of number of these networks
		output = [neuralNetwork() for x in range(number)]
		for network in output:
			for layer, count in zip(self.neuralNodes, range(len(self.neuralNodes))):
				network.neuralNodes.append([])
				for node in layer:
					network.neuralNodes[count].append(node.evolveNode())
		return output


# Example usage: randomNetwork([32,40,10,1])
	def randomNetwork(self, layersInfo): #Generates a random network, given an array of node distribution
# For the first group
		self.neuralNodes.append([])
		for x in range(layersInfo[0]):
			self.neuralNodes[0].append(neuralNode(number=1))

# Now for the rest
		def addLayer(curLayer, prevLayer):
			result = []
			for node in range(curLayer):
				result.append(neuralNode(number=prevLayer))
			return result

		for layer in itertools.starmap(addLayer, zip(layersInfo[1:], layersInfo)):
			self.neuralNodes.append(layer)

# For running from the command line, eventually
if __name__ == "__main__":
	pass
