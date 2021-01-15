# // https://leetcode.com/problems/image-smoother/
# //
# //Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

# //Example 1:
# //Input:
# //[[1,1,1],
# //[1,0,1],
# //[1,1,1]]
# //Output:
# //[[0, 0, 0],
# //[0, 0, 0],
# //[0, 0, 0]]
# //Explanation:
# //For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# //For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# //For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# //the average should be computed from the state of the ORIGINAL matrix. So, for example, after getting the average for the middle cell, if that cell's value changes, you still want to use the original value when calculating the averages for that cell's neighbors.

# //And the numbers can be from [1,255] not just 0 and 1.
# //ex:
# //[[1, 3, 2],
# //[6, 2, 25]
# //should produce
# //[3, 6, 8],
# //[3, 6, 8]

# //Remember to include the cell in its own average.
