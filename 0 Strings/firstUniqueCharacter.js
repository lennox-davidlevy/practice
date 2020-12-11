// Given a string, find the first non - repeating character in it and return it's index. If it doesn't exist, return -1.

// Examples:

// s = "leetcode"
// return 0.

// s = "loveleetcode",
// return 2.

const firstUnique = str => {
  let hash = {};
  for (let i = 0; i < str.length; i++) {
    if (hash[str[i]] === undefined) {
      hash[str[i]] = 1;
    } else {
      hash[str[i]] += 1;
    }
  }
  for (let i = 0; i < str.length; i++) {
    if (hash[str[i]] === 1) {
      return str[i];
    }
  }
  return -1;
};

let result = firstUnique('aabbccdeeffghii');
