import numpy as np

class DataGenerator:

	def __init__(self, num):
		self.num = num
		self.train_data = []
		self.target_data = []

	def logic_data(self):

		for i in range(self.num):
			self.train_data.append([np.random.choice(2), np.random.choice(2)])

		for i in self.train_data:
			self.target_data.append([i[0] or i[1]])

		return { 'train_data': self.train_data, 
				 'target_data' : self.target_data }

		def double_data(self):
			pass