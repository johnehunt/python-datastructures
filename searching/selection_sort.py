# Part 3: Selection Sort
# The selection sort improves on the bubble sort by
# making only one exchange for every pass through the list.
# In order to do this, a selection sort looks for the
# largest value as it makes a pass and, after completing
# the pass, places it in the proper location.
# Each subsequent pass places the next value in the correct
# location until all values are correctly placed

print('-' * 40)
print('Example of the Selection Sort Algorithm')
print('-' * 40)


def selection_sort(data_list):
    for slot_to_fill in range(len(data_list) - 1, 0, -1):
        position_to_swap = 0
        for location in range(1, slot_to_fill + 1):
            if data_list[location] > data_list[position_to_swap]:
                position_to_swap = location
        if position_to_swap != slot_to_fill:
            print(f'Swapping {data_list[position_to_swap]} '
                  f'with {data_list[slot_to_fill]} '
                  f'from {position_to_swap} '
                  f'to slot {slot_to_fill}')
            temp = data_list[slot_to_fill]
            data_list[slot_to_fill] = data_list[position_to_swap]
            data_list[position_to_swap] = temp


data = [93, 77, 54, 20, 17]
print('Initial data list -', data)

selection_sort(data)

print('Final data list -', data)

# Redueced down to two swaps
# Although similar number of comparisons to bubble sort O(n2)