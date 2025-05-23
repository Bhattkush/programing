def two_sum(nums, target):
    """
    Returns a tuple of indices of the two numbers in 'nums' that add up to 'target'.
    """
    seen = {}  # Dictionary to store number: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)  # Return indices as a tuple
        seen[num] = i

# Generate the list [1, 2, ..., 1_000_000]
nums = list(range(1, 1_000_001))

# Set the target such that 2 + 1_000_000 = 1_000_002
target = 1_000_002

# Call the function
result = two_sum(nums, target)

# Print the result
print("Indices of numbers that add up to", target, ":", result)
