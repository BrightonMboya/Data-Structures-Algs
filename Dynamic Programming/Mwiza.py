def minimumWaitingTime(queries):
	# Write your code here.
	queries.sort()
	waitingTime = 0
	for i in range(len(queries)-1):
		waitingTime += waitingTime + queries[i]
	return waitingTime

print(minimumWaitingTime([5, 4, 3, 2, 1]))