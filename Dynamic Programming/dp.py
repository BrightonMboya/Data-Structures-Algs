def bestSum(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    shortestCombination= None
    for num in numbers:
        remainder = targetSum - num
        remainderCombination = bestSum(remainder, numbers)

        if remainderCombination != None:
            combination = [*remainderCombination, num]

        if shortestCombination == None and len(combination) < len(shortestCombination):
            shortestCombination = combination
    return shortestCombination

print(bestSum(7, [5,3,4,7]))
print(bestSum(8, [2,3,5]))
print(bestSum(8, [1,4,5]))
print(bestSum(100, [1,2,5,25]))
