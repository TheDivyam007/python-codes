def find_missing_number(lst, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

# Example usage
print(find_missing_number([1, 2, 4, 5, 6], 6))  # Output: 3
