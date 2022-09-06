def solution(x, y):
    # Restrict the number of Worker Cells.
    if ((x < 1 or x > 100000) or (y < 1 or y > 100000)):
        return "The co-ordinates of the cell location (x, y) must be between 1 and 100000 (inclusive)."

    # The initial increment value. The increment value is not re-initialised when moving across/up the Worker Cell locations.
    increment = 1

    # Determine the Worker Id of the X co-ordinate.
    for r in range(1, x+1):
        # The first Worker Id of the X co-ordinate is always 1.
        if (r == 1):
            workder_id_x = 1

        # Iterate and increment through all of the X co-ordinates.
        else:
            workder_id_x = increment + workder_id_x + 1
            increment += 1 

    # Assign the Worker Id to iterate through the Y co-ordinates.
    worker_id = workder_id_x 
    for c in range(1, y):
        worker_id = increment + worker_id
        increment += 1

    # Return the Worker Id.
    return str(worker_id)


print(solution(1, 1)) # 1
print(solution(1, 2)) # 2
print(solution(2, 1)) # 3
print(solution(2, 3)) # 8
print(solution(3, 2)) # 9
print(solution(6, 6)) # 61
print(solution(5, 10)) # 96
print(solution(320, 99999)) # 5031800723
print(solution(-12, 5))
print(solution(100000, 100001))