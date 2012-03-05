"""Function that evaluates a given board and returns a value based on the configuration of the neural network
Ben Hartman 3/4/2012
"""

import board
import neuralNetwork


SCALINGFACTOR = .5 #Used by the evolver to modify the resultant weight distribution
EVOLVERSTANDARDDEVIATION = 1
SQRTEVOLVERSTANDARDDEVIATION = math.sqrt(EVOLVERSTANDARDDEVIATION)

# For running from the command line, eventually
if __name__ == "__main__":
	pass
