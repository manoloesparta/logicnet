# Logic Neural Network

This is a 2 hidden layer neural network made with love :)
This was original made for learning logical gates but you can use with any normalized data.

## Requirements
```
pip install -r requirements.txt
```

## Usage

#### Instance of a neural network
```python
from neuralnetwork import NeuralNetwork

input_nodes = 2
hidden_layer1_nodes = 100
hidden_layer2_nodes = 100
output_nodes = 1
learning_rate = 0.3

ann = NeuralNetwork(input_nodes, hidden_layer1_nodes, hidden_layer2_nodes, output_nodes, learning_rate)
```

#### Creating the data for the neural network
NOTE: *The only data it creates is about logical gates using the functions AND or OR. If you want to use your own data, you need to your normalize data and feed it to the network*
```python
from data import DataGenerator

num_samples = 100

data =  DataGenerator(num_samples).generate_data()
x = data['train_data']
y = data['target_data']
```

#### Training neural network
```python
epochs = 1000

ann.train(x,y, epochs)
```

#### Predicting
```python
unknown_answer = [[0,1]]

ann.predict(unknown_answer)
```