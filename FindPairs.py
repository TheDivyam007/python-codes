def find_pairs(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

# Example usage
print(find_pairs([1, 2, 3, 4, 5, 6], 7))  # Output: [(3, 4), (2, 5), (1, 6)]
