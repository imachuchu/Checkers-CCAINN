# Function that evaluates a given board and returns a value based on the configuration of the neural network

class board():
	location = [] # There are 32 spots on a checker board, each spot is either e, r, b, R, B (empty, red, black, red king, black king)

# Contains a neural network, which consists of multiple layers, each layer consists of multiple nodes each one connected to each node from the previous layer
class neuralNetwork():
	weights = []

	def evaluateLayer(previous, currentLayer): #evaluates one layer, and calls itself on the next
		for node in weights[currentLayer]:
			result.append(reduce(lambda x,y: x+y, map(lambda x,y: x*y, node, previous)))
		if currentLayer+1 == length(weights): # If we are on the last layer
			return result[0] # The last layer only has one node
		else:
			evaluateLayer(result, currentLayer+1) # Not tail recursive, which stinks, but we shouldn't have too many layers

	def evaluateBoard(board): #Evaluates a board and returns how much the neural network likes it
		result = map(lambda x,y: x*y, zip(weights[0], board.location))
		return evaluateLayer(result, 1)


if __name__ == "__main__":

