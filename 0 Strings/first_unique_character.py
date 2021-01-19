# // Given a string, find the first non - repeating character in it and return it's index. If it doesn't exist, return -1.

# // Examples:

# // s = "leetcode"
# // return 0.

# // s = "loveleetcode",
# // return 2.
from collections import defaultdict


def first_unique(string):
    if len(string) == 0:
        return None
    if len(string) == 1:
        return string[0]
    char_hash = defaultdict(int)
    for char in string:
        char_hash[char] += 1
    print(char_hash)


first_unique("leetcode")
print("fun")
