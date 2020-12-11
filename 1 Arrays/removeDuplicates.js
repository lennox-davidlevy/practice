// Given nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
// Your function should return length = 5, with the first five elements of
// nums being modified to 0, 1, 2, 3, and 4 respectively.
// It doesn't matter what values are set beyond the returned length.

//count unique nums
const removeDuplicates = nums => {
  if (nums.length === 0) {
    return 0;
  }
  if (nums.length === 1) {
    return 1;
  }
  let count = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== nums[i + 1]) {
      count++;
      nums[count] = nums[i + 1];
    }
  }
  return count;
};
//removeDupes return arr;
const removeDuplicates = arr => {
  return arr.filter((ele, idx) => {
    return arr.indexOf(ele) !== idx;
  });
};
