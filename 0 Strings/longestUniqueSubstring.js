// Given a string s, find the length of the longest substring without repeating characters.

// Example 1:

// Input: s = "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
// Example 2:

// Input: s = "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
// Example 3:

// Input: s = "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
// Example 4:

// Input: s = ""
// Output: 0

const lengthOfLongestSubstring = (str) => {
  let len = str.length;
  let set = new Set();
  let result = 0,
    i = 0,
    j = 0;
  while (i < len && j < len) {
    if (!set.has(str.charAt(j))) {
      set.add(str.charAt(j++));
      result = Math.max(result, j - i);
    } else {
      set.delete(str.charAt(i++));
    }
  }
  return result;
};
