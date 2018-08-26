from neuralnetwork import NeuralNetwork
from data import DataGenerator

ann = NeuralNetwork(2, 100, 100, 1, 0.1)

data = DataGenerator(10).generate_data()

train_data = data['train_data']
target_data = data['target_data']

print(target_data)

ann.train(train_data, target_data, 10000)
ann.predict([[0,1]])