def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
print(is_anagram("listen", "silent"))  # Output: True
print(is_anagram("hello", "world"))   # Output: False
