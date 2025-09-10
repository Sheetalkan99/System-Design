def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}  # base case: one way to get sum 0

    for num in nums:
        prefix_sum += num

        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]

        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count

# Example usage
nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))  # This will correctly print the result
