from random import choice

class DataGenerator:

	def __init__(self, num):
		self.num = num
		self.train_data = []
		self.target_data = []

	def logic_data(self):
		options = [0, 1]
		self.train_data = [[choice(options), choice(options)] for _ in range(self.num)]
		self.target_data = [[i[0] or i[1]] for i in self.train_data]

		return {
			'train_data': self.train_data,
			'target_data' : self.target_data
		}
