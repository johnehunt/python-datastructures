# Part 1: Bubble Sort
# The bubble sort makes multiple passes through a list.
# It compares adjacent items and exchanges those that are
# out of order. Each pass through the list places the next
# largest value in its proper place. In essence, each item
# “bubbles” up to the location where it belongs.

print('-' * 36)
print('Example of the Bubble Sort Algorithm')
print('-' * 36)


def bubble_sort(data_list):
	pass_number = 0
	for i in range(len(data_list) - 1, 0, -1):
		pass_number += 1
		print(f'Pass {pass_number} through the data')
		for j in range(0, i):
			if data_list[j] > data_list[j + 1]:
				temp = data_list[j]
				data_list[j] = data_list[j + 1]
				data_list[j + 1] = temp
			print(f'\tData at end of pass {pass_number}.{j} - {data_list}')


data = [93, 77, 54, 20, 17]
print('Initial data list -', data)

bubble_sort(data)

print('Final data list -', data)

# Note the effect of each pass through the data
# Where n = 5 (length of list of data)
# Pass 1 => n - 1 comparisons
# Pass 2 => n - 2 comparisons
# Pass 3 => n - 3 comparisons
# Pass 4 => n - 4 comparisons
