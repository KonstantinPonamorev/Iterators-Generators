nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

		def __init__(self, list):
			self.list = nested_list
			self.start = 0
			self.end = len(self.list) - 1

		def __iter__(self):
			return self

		def __next__(self):
			self.start += 1
			if self.start == self.end:
				raise  StopIteration
			else:
				for item in self.list:
					for item_2 in item:
						print(item_2)





if __name__ == '__main__':
	for item in FlatIterator(nested_list):
		print(item)
	flat_list = [[item for item in FlatIterator(nested_list)]]
	print(flat_list)


