"""
Input:  s = "abcabcbb"
Output: 3
Question: Given a string s, find the length of the longest substring without repeating characters.
Explanation: The longest substrings without repeating characters are "abc", each of length 3.

Usage: Arrays, hashmaps, sliding window
Approach: Use a sliding window technique to track the characters and their indices.

Keep in mind storing the substrings in hash maps eats up extra memory.we only care about the length of the longest substring.
# Time Complexity: O(n)

Hint: Use enumerate function to get the index and character in the string.
"""

#Method1 - Brute Force
"""
construct a substring from starting index and get all substrings
with that and move on e and get all substrings with next index
and so on.
complexity: O(n^2)

Use sets if  possible for brute force
"""
             #0123456
teststring = "abcabcdbbcdefga"
string_len = len(teststring)

def length_of_longest_substring(teststring: str) -> int:
    """
    Function to find the length of the longest substring without repeating characters.
    Input:  s = "abcabc"
    """

    max_length = 0
    max_substring = ""

    for start_index in range(string_len):
        print("Starting index is %s"% start_index)

        for current_index in range (start_index, string_len):
            print("Current index is %d" %current_index)

            substring = teststring[start_index : current_index + 1]
            next_char = teststring[current_index]

            print("checking if element {} is in {}".format(next_char, substring))

            if next_char in substring[:-1]:
                break

            current_len = current_index - start_index +1

            if max_length < current_len:
                max_length = current_len
                max_substring = substring

    return max_length, max_substring

max_length, max_substring = length_of_longest_substring(teststring)
print("Max length is %d of substring %s"% (max_length, max_substring))