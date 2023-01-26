def find_duplicate(nums):
    nums.sort()

    for index in range(1, len(nums)):
        if type(nums[index]) is str:
            return False
        elif len(nums) < 2 or nums[index] < 0:
            return False
        elif nums[index] == nums[index - 1]:
            return nums[index]

    return False
