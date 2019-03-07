from ann.neuralnetwork import NeuralNetwork
from ann.data import DataGenerator

def main():
    ann = NeuralNetwork(2, 100, 100, 1, 0.1)

    data = DataGenerator(100).logic_data()

    train_data = data['train_data']
    target_data = data['target_data']

    ann.train(train_data, target_data, 10000)
    ann.predict([[0,1]])

if __name__ == '__main__':
   main()
