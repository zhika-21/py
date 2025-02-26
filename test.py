def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(nums)  # Sum of given numbers
    return expected_sum - actual_sum  # The missing number

# Example usage
print(find_missing_number([3, 0, 1]))  # Output: 2
print(find_missing_number([0, 1]))     # Output: 2
print(find_missing_number([9,6,4,2,3,5,7,0,1]))  # Output: 8
