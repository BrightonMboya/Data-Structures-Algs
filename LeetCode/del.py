def threeNumberSort(array, order):
	# Write your code here.
	k = 3
	while k <= 3:
		currentNum = order.pop(0)
		newPos = 0
		left = newPos
		for i in range(1, len(array)):
			if array[left] == currentNum:
				left += 1
				newPos += 1
			if array[i] == currentNum:
				array[left], array[i] = array[i], array[left]
				left += 1
				newPos += 1
		k -= 1
	return array

# 0 0 0 1 1 -1 -1

threeNumberSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1])