def insert_squares(arr, num):
# add square of numbers from 1 to num to the list named arr and return list
	for i in range(1, num + 1):
		num_1 = i * i
		arr.append(num_1)
	return arr