"""
Have the function MaximumSquare(strArr) take the strArr parameter being passed which will be a 2D matrix 
of 0 and 1's, and determine the area of the largest square submatrix that contains all 1's. 
A square submatrix is one of equal width and height, and your program should return the area of the 
largest submatrix that contains only 1's. For example: if strArr is ["10100", "10111", "11111", "10010"] 
then this looks like the following matrix: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0 

For the input above, you can see that the largest square submatrix is of size 2x2, so your program should 
return the area which is 4. 
You can assume the input will not be empty. 
"""


def MaximumSquare(strArr):
    # Your code goes here
    max_step = 1

    for x in range(0, len(strArr) + 1):
        for y in range(0, len(strArr[0]) + 1):
            while check_square(strArr, (x, y), max_step):
                max_step += 1

    return (max_step - 1) ** 2

def check_square(strArr, point, check_size):
    square = True
    if point[0] + check_size > len(strArr[0]) or point[1] + check_size > len(strArr):
        return False

    for x in range(point[0], point[0] + check_size):
        for y in range(point[1], point[1] + check_size):
            try:
                if int(strArr[x][y]) != 1:
                    square = False
                    break
            except IndexError:
                square = False
                break

    return square