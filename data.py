import numpy as np

class DataGenerator:

	def __init__(self, num):
		self.num = num
		self.train_data = []
		self.target_data = []

	def generate_train_data(self):
		for i in range(self.num):
			self.train_data.append([np.random.choice(2), np.random.choice(2), np.random.choice(2)])
		return np.array(self.train_data)

	def generate_target_data(self):
		for i in self.train_data:
			if i[2] == 0:
				self.target_data.append([i[0] and i[1]])
			elif i[2] == 1:
				self.target_data.append([i[0] or i[1]])
		return np.array(self.target_data)