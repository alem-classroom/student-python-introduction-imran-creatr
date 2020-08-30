def insert_squares(arr, num):
	i = 1
	while i < num + 1:
		num_1 = i * i
		i = i + 1
		arr.append(num_1)
	return arr
    # add square of numbers from 1 to num to the list named arr and return list