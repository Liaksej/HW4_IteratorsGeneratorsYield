def flat_generator(list_of_lists: list):
    list_1_position = 0
    list_2_position = 0
    while list_1_position < len(list_of_lists):
        cursor = list_of_lists[list_1_position][list_2_position]
        yield cursor
        list_2_position += 1
        if list_2_position == len(list_of_lists[list_1_position]):
            list_1_position += 1
            list_2_position = 0


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    for item in flat_generator(nested_list):
        print(item)
