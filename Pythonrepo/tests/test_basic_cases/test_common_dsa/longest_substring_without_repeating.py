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


Method1 - Brute Force - No sliding window

complexity: O(n^2)

Use sets if  possible for brute force
"""


print("\n\nMethod1 - Brute Force - O(n\u00b2)")


#              #0123456
test_string = "abcdbea"
string_len = len(test_string)

def length_of_longest_substring(test_str: str) -> int:
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

            substring = test_str[start_index : current_index + 1 ]
            next_char = test_str[current_index]

            if next_char in substring[:-1]:
                break

            current_len = current_index - start_index +1

            if max_length < current_len:
                max_length = current_len
                max_substring = substring

    return max_length, max_substring

max_length, max_substring = length_of_longest_substring(test_string)
print("Max length is %d of substring %s"% (max_length, max_substring))



"""
Method2 - sliding window - O(n)
"""
def longest_subsequence_sliding():
    print("\n\n Method2 - sliding window - O(n)")

    seen = set()
    left = 0
    max_substring = ""
    max_length = 0

    for right in range(string_len):
        while test_string[right] in seen:
            seen.remove(test_string[left])
            left +=1

        seen.add(test_string[right])
        print(seen)

        if max_length < right - left + 1:
            max_length = right - left + 1
            max_substring = test_string[left : right + 1]

    print("Max length is %d of substring %s"%(max_length , max_substring))

longest_subsequence_sliding()



"""
Method 3: Last Seen Index with HashMap (Same logic, different thinking)
"""
print("\n\n Last Seen Index with HashMap (Same logic, different thinking")

def longest_unique_with_last_seen(s):
    last_seen = {}
    start = 0
    max_len = 0
    max_substring = ""

    for i, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
            print("start is %s"%char)
        last_seen[char] = i
        print("Last seen: %s"%last_seen)

        if max_len < i - start + 1:
            max_len = i - start + 1
            max_substring = s[start:i+1]

    print("Max length is %d of substring '%s'" % (max_len, max_substring))

longest_unique_with_last_seen(test_string)