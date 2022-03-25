nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = 0
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if len(self.main_list[self.main_list_cursor]) == self.nested_list_cursor:
            self.main_list_cursor += 1
            self.nested_list_cursor = 0
        if self.main_list_cursor > len(self.main_list):
            raise StopIteration
        return self.main_list[self.main_list_cursor][self.nested_list_cursor]




def flat_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item


if __name__ == '__main__':
    # for item in flat_generator(nested_list):
    #     print(item)
    # flat_list = [item for item in flat_generator(nested_list)]
    # print(flat_list)
	for item in FlatIterator(nested_list):
		print(item)
	# 	flat_list = [[item for item in FlatIterator(nested_list)]]
	# print(flat_list)
