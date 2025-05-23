def two_sum_dict(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            # Return the result as a dictionary instead of a tuple
            return {"index1": seen[complement], "index2": i}
        seen[num] = i

# Generate the list [1, 2, ..., 1_000_000]
nums = list(range(1, 1_000_001))

# Set the target such that 2 + 1_000_000 = 1_000_002
target = 1_000_002

# Call the function
result = two_sum_dict(nums, target)

# Print the result in dictionary format
print("Indices of numbers that add up to", target, ":", result)
