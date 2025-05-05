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

teststring = "abcdbea"
string_len = len(teststring)
max_substring = ""

def length_of_longest_substring(teststring: str) -> int:
    """
    Function to find the length of the longest substring without repeating characters.
    Input:  s = "abcabcbb"
    """

    new_length = 0
    new_substring = ""
    max_length = len(teststring[0])
    max_substring = teststring[0]

    for start_index in range(len(teststring)):
        print("Starting index is %s"% start_index)

        for current_index in range (start_index , string_len):
            print("Current index is %d" %current_index)

            next_index = current_index + 1

            if next_index > string_len:
                break

            if teststring[next_index] in teststring[start_index : current_index]:
                new_length = len(teststring[start_index :current_index +1])
                new_substring = teststring[start_index :current_index +1 ]

                print("Coming into inner loop Max old lenght was :%d" %max_length)

                if max_length < new_length:
                    max_length = new_length
                    max_substring = new_substring

                print("Inner loop for index %s New length is %d of string: %s" % (start_index, new_length, new_substring))
                print("Inner loop for index %s Max length is %d of string: %s" % (start_index, max_length, max_substring))
                break

        print("outer loop for index %s New length is %d of string: %s\n\n" % (start_index, max_length, max_substring))
        continue

    return max_length, max_substring

max_length, max_substring = length_of_longest_substring(teststring)
print("Max lenght is %d of substring %s"% (max_length, max_substring))