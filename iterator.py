class FlatIterator(list):

    def __iter__(self):
        self.list_1 = 0
        self.list_2 = 0
        return self

    def __next__(self):
        if self.list_1 == len(self):
            raise StopIteration
        if self.list_1 == len(self) + 1:
            raise StopIteration
        self.cursor = self[self.list_1][self.list_2]
        self.list_2 += 1
        if self.list_2 == len(self[self.list_1]):
            self.list_1 += 1
            self.list_2 = 0
        print(self.cursor)
        return self.cursor


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
