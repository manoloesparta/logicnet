import numpy as np

class NeuralNetwork:
	
	def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
		self.input_nodes = input_nodes
		self.hidden_nodes = hidden_nodes
		self.output_nodes = output_nodes

		self.learning_rate = learning_rate

		self.weights_input_hidden = np.random.randn(self.hidden_nodes, self.input_nodes)
		self.weights_hidden_output = np.random.randn(self.output_nodes, self.hidden_nodes)

	def train(self, train_data, target_data, epochs):
		for i in range(epochs):

			inputs = np.array(train_data, ndmin=2).T
			targets = np.array(target_data).T

			hidden_inputs = np.matmul(self.weights_input_hidden, inputs)
			hidden_outputs = NeuralNetwork.sigmoid(hidden_inputs)

			final_inputs = np.matmul(self.weights_hidden_output, hidden_outputs)
			final_outputs = NeuralNetwork.sigmoid(final_inputs)

			output_error = (targets - final_outputs) ** 2
			hidden_error = np.matmul(self.weights_hidden_output.T, output_error)

			self.weights_hidden_output += self.learning_rate * np.matmul(NeuralNetwork.dsigmoid(final_inputs), hidden_outputs.T)
			self.weights_input_hidden += self.learning_rate * np.matmul(NeuralNetwork.dsigmoid(hidden_inputs), inputs.T)

		return 'trained'
	
	def predict(self, predict_data):
		inputs = np.array(predict_data, ndmin=2).T

		hidden_inputs = np.matmul(self.weights_input_hidden, inputs)
		hidden_outputs = NeuralNetwork.sigmoid(hidden_inputs)

		final_inputs = np.matmul(self.weights_hidden_output, hidden_outputs)
		final_outputs = NeuralNetwork.sigmoid(final_inputs)

		return final_outputs

	@staticmethod
	def sigmoid(x):
		return 1 / (1 + np.exp(-x))

	@staticmethod
	def dsigmoid(x):
		return NeuralNetwork.sigmoid(x) * (1 - NeuralNetwork.sigmoid(x))

if __name__ == '__main__':
	
	ann = NeuralNetwork(2,10,1,0.2)
	ann.train([[0,1]],[0],100)

	print(ann.predict([0,1]))