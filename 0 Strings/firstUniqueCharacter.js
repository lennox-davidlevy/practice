// Given a string, find the first non - repeating character in it and return it's index. If it doesn't exist, return -1.

// Examples:

// s = "leetcode"
// return 0.

// s = "loveleetcode",
// return 2.

const firstUnique = (str) => {
  if (str.length === 0) return -1;
  if (str.length === 1) return 0;
  const dict = {};
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    dict[char] = dict[char] + 1 || 1;
  }
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    if (dict[char] === 1) return i;
  }
  return -1;
};


