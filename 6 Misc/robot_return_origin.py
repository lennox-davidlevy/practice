# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

# Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.


# Example 1:

# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
# Example 2:

# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.
# Example 3:

# Input: moves = "RRDD"
# Output: false
# Example 4:

# Input: moves = "LDRRLRUULR"
# Output: false


# def robot_return(directions):
#    if len(directions) == 0 or len(directions) == 1:
#        return False
#    location = [0, 0]
#    for char in directions:
#        if char == "L":
#            location[0] -= 1
#        elif char == "R":
#            location[0] += 1
#        elif char == "D":
#            location[1] -= 1
#        else:
#            location[1] += 1
#    return location[0] == 0 and location[1] == 0


def robot_return(moves):
    L = moves.count("L")
    R = moves.count("R")
    U = moves.count("U")
    D = moves.count("D")
    return L == R and U == D


print(robot_return("UD"))
print(robot_return("LL"))
print(robot_return("RRDD"))
print(robot_return("LDRRLRUULR"))