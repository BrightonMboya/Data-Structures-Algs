nums = [5, 1, 2, 3, 4]
n = len(nums)
for inx in reversed(range(n-1)):
    nums[inx], nums[inx-1] = nums[inx-1], nums[inx]
print(nums)