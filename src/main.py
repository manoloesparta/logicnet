from neuralnetwork import NeuralNetwork
from data import DataGenerator

ann = NeuralNetwork(2, 10, 1, 0.3)

data = DataGenerator(1000).generate_data()

train_data = data['train_data']
target_data = data['target_data']