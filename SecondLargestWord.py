def second_largest(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort(reverse=True)
    return unique_lst[1] if len(unique_lst) > 1 else None

# Example usage
print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
