# A bubble sort is often considered the most inefficient
# sorting method since it must exchange items before the final
# location is known. These “wasted” exchange operations are very
# costly. However, because the bubble sort makes passes through
# the entire unsorted portion of the list, it has the capability
# to do something most sorting algorithms cannot. In particular,
# if during a pass there are no exchanges, then we know that the
# list must be sorted. A bubble sort can be modified to stop early
# if it finds that the list has become sorted.

print('-' * 50)
print('Example of the "short Cut" Bubble Sort Algorithm')
print('-' * 50)


def short_cut_bubble_sort(data_list):
	pass_number = 0
	for i in range(len(data_list) - 1, 0, -1):
		exchanges = False
		pass_number += 1
		print(f'Pass {pass_number} through the data')
		for j in range(0, i):
			if data_list[j] > data_list[j + 1]:
				exchanges = True
				temp = data_list[j]
				data_list[j] = data_list[j + 1]
				data_list[j + 1] = temp
			print(f'\tData at end of pass {pass_number}.{j} - {data_list}')
		if not exchanges:
			break


data = [17, 20, 24, 93, 77]
print('Initial data list -', data)

short_cut_bubble_sort(data)

print('Final data list -', data)

# Note the effect of each pass through the data
# Where n = 5 (length of list of data)
# Pass 1 => n - 1 comparisons
# Pass 2 => n - 2 comparisons
# break
