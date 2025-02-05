from collections import Counter

def word_frequency(s):
    words = s.split()
    return dict(Counter(words))

# Example usage
print(word_frequency("apple banana apple orange banana apple"))  
# Output: {'apple': 3, 'banana': 2, 'orange': 1}
