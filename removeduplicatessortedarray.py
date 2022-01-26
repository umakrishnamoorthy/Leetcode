#remove the duplicates in an sorted array - the number should be unique in an array with no repeated numbers, these are arranged in non-decresing order
def removeduplicate(self, nums):
    length = 1
    if len(nums) == 0:
        return 0
    for i in range(1, len(nums)):
        if len(nums) != nums[i-1]:
            nums[length] = nums [i]
            length += 1
        return length
