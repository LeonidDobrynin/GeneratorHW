
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

# class FlatIterator:
#
# 	def __init__(self,lists):
# 		self.lists = lists
# 		self.check = -1
#
# 	def __iter__(self):
# 		iter_list = []
# 		for j in self.lists:
# 			for s in j:
# 				iter_list.append(s)
# 		self.cursor = iter_list[0]
# 		return  self
#
# 	def __next__(self):
# 		iter_list = []
# 		for j in self.lists:
# 			for s in j:
# 				iter_list.append(s)
# 		self.check += 1
# 		# index = iter_list.index(self.cursor)
#
# 		if self.check == iter_list.index(iter_list[-1]):
# 			raise StopIteration
#
#
# 		self.cursor = iter_list[self.check]
# 		return self.cursor
#
#
#
#
#
# for item in FlatIterator(nested_list):
# 	print(item)


def flat_generator(itered_list):
	iter_list = []
	for j in itered_list:
		for s in j:
			iter_list.append(s)
	x = 0
	iter_flat = iter_list[x]
	while x != len(iter_list):
		if iter_list[x] == iter_list[-1]:

			yield iter_flat
			x += 1
		else:
			yield iter_flat
			x += 1
			iter_flat = iter_list[x]



for item in  flat_generator(nested_list):
	print(item)
