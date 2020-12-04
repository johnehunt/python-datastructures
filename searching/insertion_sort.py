# Part 4: Insertion Sort
# The insertion sort splits a list into two, the sorted part
# and the unsorted part.
# The sorted part is treated as the start of the list - the sorted sublist.
# Each new item is then “inserted” back into the correct position in the
# previous sorted sublist until the sorted sublist is the whole list.

print('-' * 40)
print('Example of the Insertion Sort Algorithm')
print('-' * 40)


def insertion_sort(data_list):
	# Loop over the whole data list
	for index in range(1, len(data_list)):
		# Current starting position in unsorted list
		current_value = data_list[index]
		print(f'Current value {current_value} at index {index}')
		position = index
		# Find where in the sorted sublist the value should be placed
		while position > 0 and data_list[position - 1] > current_value:
			print(f'\tmoving {data_list[position -1]} at {position -1} to {position}')
			data_list[position] = data_list[position - 1]
			position = position - 1

		print(f'\tsetting {position} to {current_value}')
		data_list[position] = current_value


data = [93, 15, 77, 54, 20]
print('Initial data list -', data)

insertion_sort(data)

print('Final data list -', data)
