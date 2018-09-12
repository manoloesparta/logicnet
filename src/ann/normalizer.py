import numpy as np

class Normalizer:

	def __init__(self, data):
		self.data = data

	def normalize(self, min, max):
		pass

	def denormalize(self):
		pass


if __name__ == '__main__':

	from neuralnetwork import NeuralNetwork

	ann = NeuralNetwork(1,10,10,1,0.3)
	n = Normalizer(np.array([0,1]))
	n.normalize()