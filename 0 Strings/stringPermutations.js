// Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

// Example 1:

// Input: s1 = "ab" s2 = "eidbaooo"
// Output: True
// Explanation: s2 contains one permutation of s1 ("ba").
// Example 2:

// Input:s1= "ab" s2 = "eidboaoo"
// Output: False

const checkInclusion = (s1, s2) => {
  if (!s1 || !s2 || s1.length > s2.length) return false;
  const n = s1.length;
  const dict = {};
  for (let i = 0; i < n; i++) {
    const char = s1[i];
    dict[char] = dict[char] + 1 || 1;
  }
  for (let i = 0; i < s2.length; i++) {
    let subString = s2.slice(i, n + i);
    if (subString.length < n) return false;
    if (stringCheck({ ...dict }, subString)) return true;
  }
  return false;
};

const stringCheck = (dict, subString) => {
  for (let i = 0; i < subString.length; i++) {
    const char = subString[i];
    if (!dict[char]) return false;
    dict[char] -= 1;
  }
  return true;
};
