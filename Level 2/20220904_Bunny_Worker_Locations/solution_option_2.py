import numpy

def solution(x, y):
    # Restrict the scope of number of Worker Cells.
    if ((x < 1 or x > 100000) or (y < 1 or y > 100000)):
        return "The co-ordinates of the cell location (x, y) must be between 1 and 100000 (inclusive)."

    # The array variables will be inverted for easier row and column references. This is due to the stacked triangular shape of the cell layout. 
    arr_x = y
    arr_y = x

    # Initialise an empty array with the given cell points.
    array = numpy.zeros((arr_x,arr_y), dtype=int)

    # Populate the Worker Id's for every cell in the array.
    for r in range(0, arr_x):
        for c in range(0, arr_y):
            # Most frequent case should be evaluated first to speed up the code. Loops through columns of each row.
            if (c > 0):
                array[r,c] = array[r,c-1] + r + c + 1

            # Ensure the first column entry on each new row is correct.
            elif (r > 0 and c == 0):
                array[r,c] = array[r-1,c] + r + c

            # Initialise the Root value.
            elif (r == 0 and c == 0):
                array[r,c] = 1

    # print(array)
    return str(array[arr_x-1, arr_y-1])


print(solution(1, 1)) # 1
print(solution(3, 2)) # 9
print(solution(2, 3)) # 8
print(solution(5, 10)) # 96
print(solution(6, 6)) # 61
# print(solution(320, 99999)) # 736833427
print(solution(-12, 5))
print(solution(100000, 100001))