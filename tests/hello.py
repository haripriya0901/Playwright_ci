# Description: Return how many times each character appears in a string.
# Example:
# Input: "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

input_str = "hello"

# Create an empty dictionary to store character counts
char_count = {}

# Loop through each character in the string
for ch in input_str:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print(char_count)