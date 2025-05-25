def two_sum(nums, target):
    num_map = {}
    """ [1,2,5,9,3,5]"""
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
        print(f"Current number: {num}, Index: {i}, Map: {num_map}")
    return []

array = two_sum([1,2,5,9,3,5], 6)
print("Indices of numbers that add up to target:", array)