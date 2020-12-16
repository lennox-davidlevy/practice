// Given a non-negative integer x, compute and return the square root of x.

// Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

// Example 1:

// Input: x = 4
// Output: 2
// Example 2:

// Input: x = 8
// Output: 2
// Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

//binary search
const squareRoot = (n) => {
  if (n === 0) return 0;
  let left = 1,
    right = Number.MAX_VALUE;
  while (true) {
    let mid = left + (right - left) / 2;
    if (mid > n / mid) {
      right = mid - 1;
    } else {
      if (mid + 1 > n / (mid + 1)) {
        return mid;
      }
      left = mid + 1;
    }
  }
};
