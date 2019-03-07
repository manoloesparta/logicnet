import numpy as np

class NeuralNetwork:

    def __init__(self, inputs_nodes, hidden_layer1, hidden_layer2, output_nodes, learning_rate):
        self.inputs_nodes = inputs_nodes
        self.hidden_layer1 = hidden_layer1
        self.hidden_layer2 = hidden_layer2
        self.output_nodes = output_nodes

        self.learning_rate = learning_rate

        self.weights_inputs_layer1 = 2 * np.random.random((self.inputs_nodes, self.hidden_layer1)) - 1 
        self.weights_layer1_layer2 = 2 * np.random.random((self.hidden_layer1,self.hidden_layer2)) - 1 
        self.weights_layer2_output = 2 * np.random.random((self.hidden_layer2,self.output_nodes)) - 1 

    def train(self, input_list, output_list, epochs):
        for i in range(epochs):
            inputs = np.array(input_list)
            outputs = np.array(output_list)

            layer1_output = NeuralNetwork.sigmoid(np.dot(inputs, self.weights_inputs_layer1))
            layer2_output = NeuralNetwork.sigmoid(np.dot(layer1_output, self.weights_layer1_layer2))
            layer3_output = NeuralNetwork.sigmoid(np.dot(layer2_output, self.weights_layer2_output))

            layer3_error = outputs - layer3_output
            layer3_delta = self.learning_rate * (layer3_error * NeuralNetwork.sigmoid(layer3_output, deriv=True))

            layer2_error = np.dot(layer3_delta, self.weights_layer2_output.T)
            layer2_delta = self.learning_rate * (layer2_error * NeuralNetwork.sigmoid(layer2_output, deriv=True))

            layer1_error = np.dot(layer2_delta, self.weights_layer1_layer2.T)
            layer1_delta = self.learning_rate * (layer1_error * NeuralNetwork.sigmoid(layer1_output, deriv=True))

            self.weights_layer2_output += layer2_output.T.dot(layer3_delta)
            self.weights_layer1_layer2 += layer1_output.T.dot(layer2_delta)
            self.weights_inputs_layer1 += inputs.T.dot(layer1_delta)

            if (i % (epochs / 10)) == 0:
                print("Error: {:.8f}".format(np.mean(np.abs(layer3_error))))

        return 'trained'

    def predict(self, input_data):
        inputs = np.array(input_data)

        layer1_output = NeuralNetwork.sigmoid(np.dot(inputs, self.weights_inputs_layer1))
        layer2_output = NeuralNetwork.sigmoid(np.dot(layer1_output, self.weights_layer1_layer2))
        layer3_output = NeuralNetwork.sigmoid(np.dot(layer2_output, self.weights_layer2_output))

        print(layer3_output)
        return layer3_output

    @staticmethod
    def sigmoid(x, deriv=False):
        if deriv == True:
            return NeuralNetwork.sigmoid(x) * (1 - NeuralNetwork.sigmoid(x))
        return 1 / (1 + np.exp(-x))