
def count_cows(nums, nums_input):
    cows = 0
    for num in nums_input:
        if num in nums:
            cows += 1
    return cows


def count_bulls(nums, nums_input):
    bulls = 0
    for i in range(len(nums_input)):
        if nums_input[i] == nums[i]:
            bulls += 1
    return bulls
