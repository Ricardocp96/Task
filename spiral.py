#Question 2 


## traversal direction and initializing the coordinates 
UP, DOWN, LEFT, RIGHT = (0, -1), (0, 1), (-1, 0), (1, 0) 
turn_right = {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP} 
# Start near the center of the matrix to produce the spiral 
def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError

    # divide the matrix by 2 to start at center     
    x, y = width // 2, height // 2 
    dx, dy = UP # initial direction is upwards -
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))


print_matrix(spiral(5, 5))