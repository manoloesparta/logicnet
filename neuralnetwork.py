import numpy as np

class NeuralNetwork:
	
	def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
		self.input_nodes = input_nodes
		self.hidden_nodes = hidden_nodes
		self.output_nodes = output_nodes

		self.learning_rate = learning_rate

		self.weights_input_hidden = np.random.randn(self.hidden_nodes, self.input_nodes) - 0.5
		self.weights_hidden_output = np.random.randn(self.output_nodes, self.hidden_nodes) - 0.5

	def train(self, train_data, target_data, epochs):
		inputs = np.array(train_data, ndmin=2).T
		targets = np.array(target_data).T

		for i in range(epochs):

			hidden_inputs = np.matmul(self.weights_input_hidden, inputs)
			hidden_outputs = NeuralNetwork.sigmoid(hidden_inputs)

			final_inputs = np.matmul(self.weights_hidden_output, hidden_outputs)
			final_outputs = NeuralNetwork.sigmoid(final_inputs)

			output_errors = (targets - final_outputs) ** 2
			hidden_errors = np.matmul(self.weights_hidden_output.T, output_errors)
			
			self.weights_hidden_output += self.learning_rate * np.matmul(output_errors * (final_outputs * (1.0 - final_outputs)), hidden_outputs.T)	
			self.weights_input_hidden += self.learning_rate * np.matmul(hidden_errors * (hidden_outputs * (1.0 - hidden_outputs)), inputs.T)

		return 'trained'
	
	def predict(self, input_data):
		inputs = np.array(input_data, ndmin=2).T

		hidden_inputs = np.matmul(self.weights_input_hidden, inputs)
		hidden_outputs = NeuralNetwork.sigmoid(hidden_inputs)

		final_inputs = np.matmul(self.weights_hidden_output, hidden_outputs)
		final_outputs = NeuralNetwork.sigmoid(final_inputs)

		return final_outputs

	@staticmethod
	def sigmoid(x):
		return 1 / (1 + np.exp(-x))

if __name__ == '__main__':
	ann = NeuralNetwork(2,30,1,0.2)
	ann.train([[0,0],[1,1]],[0,1],1000)
	print(ann.predict([0,0]))