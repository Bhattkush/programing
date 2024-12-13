class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of elements
        num_map = {}
        
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement that would satisfy the target
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_map:
                # Return the indices of the two numbers
                return [num_map[complement], i]
            
            # Store the number and its index in the dictionary
            num_map[num] = i
        
        # If no solution is found, return an empty list
        return []

# Define the input values
nums = [2, 7, 11, 15]  # Predefined list of numbers
target = 9             # Predefined target sum

# Create an instance of the Solution class and call the function
solution = Solution()
result = solution.twoSum(nums, target)

# Display the result
if result:
    print(f"Indices of the two numbers that add up to {target}: {result}")
else:
    print("No two numbers add up to the target.")
