# Function that evaluates a given board and returns a value based on the configuration of the neural network
import random #For random generation functions


class board():
	location = [] # There are 32 spots on a checker board, each spot is either e, r, b, R, B (empty, red, black, red king, black king)

	def randomBoard(self): #Generates a random board, NOTE: Will not be a valid board, just one with random stuff on it
		choices = ['e', 'r', 'b', 'R', 'B']
		for x in xrange(32):
			self.location.append(random.choice(choices))


# Contains a neural network, which consists of multiple layers, each layer consists of multiple nodes each one connected to each node from the previous layer
class neuralNetwork(object):
	weights = []

	def evaluateLayer(self, previous, currentLayer): #evaluates one layer, and calls itself on the next
		for node in self.weights[currentLayer]:
			result.append(reduce(lambda x,y: x+y, map(lambda x,y: x*y, node, previous)))
		if currentLayer+1 == length(weights): # If we are on the last layer
			return result[0] # The last layer only has one node
		else:
			return self.evaluateLayer(result, currentLayer+1) # Not tail recursive, which stinks, but we shouldn't have too many layers

	def evaluateBoard(self, board): #Evaluates a board and returns how much the neural network likes it
		result = []
		result = map(lambda x,y: x*self.getValue(y), self.weights[0], board.location)
		return self.evaluateLayer(result, 1)

	def getValue(self, piece): # Simple call that returns the value of each piece, based on our color. NOTE: currently we hard code red
		if piece == 'r':
			return 1
		if piece == 'b':
			return -1
		if piece == 'R':
			return 1.4
		if piece == 'B':
			return -1.4
		return 0


	def randomNetwork(self, layersInfo):
		results = []
		for layer in layersInfo:
			self.weights.append( map(lambda x: random.uniform(-1,1), range(layer)) )


if __name__ == "__main__":
	pass
