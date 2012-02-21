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

	def evaluateBoard(self, board): #Evaluates a board and returns how much the neural network likes it
		previous = []
		counter = 0
		previous = map(lambda x,y: x*self.getValue(y), self.weights[0], board.location)
		for layer in self.weights[1:]:
			current = []
			for node in layer:
				total = 0
				for num in len(node):
					total += node[num] * previous[num]
				current.append(total)
				#current.append(sum(map(lambda x,y: x*y, node, previous)))
			previous = current
		return previous

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
		self.weights.append([])
		for x in range(layersInfo[0]):
			self.weights[0].append(random.uniform(-1,1))
		for layer in layersInfo[1:]:
			array = map(lambda x: random.uniform(-1,1), range(layer))
			self.weights.append(array)

if __name__ == "__main__":
	pass
