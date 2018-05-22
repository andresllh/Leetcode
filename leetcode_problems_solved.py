# Problem 1: Two Sum
def twoSum(self, nums, target)
	for i in range(len(nums)):
		for j in range(len(nums)):
			if j == i:
				continue
			if nums[i] + nums[j] == target:
				return [i, j]

# Problem 7: Reverse Integer
def reverse_integer(self, x):
    import numpy as np
    """
    :type x: int
    :rtype: int
    """
    x = str(x)
    x = x[::-1]
    if x[-1] is '-':
        x = '-' + x[:-1]
    x = int(x)
    if np.abs(x) > 2**31 - 1:
        return 0
    return x
