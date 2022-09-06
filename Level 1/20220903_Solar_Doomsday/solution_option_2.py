import math

def solution(area, solar_panels=None):
    # Restrict the scope of the total solar panel area.
    if (area < 1 or area > 1000000):
        return "The total area of solar panels must be between 1 and 1000000 (inclusive)."

    # If a list of sqaure solar panels has not been passed as argument, create an empty one.
    if (solar_panels is None):
        solar_panels = []

    # Return the list of sqaure solar panels when there are no more solar panels to allocate.
    if (area == 0):
        return solar_panels

    # Assign square solare panels to the given area.
    else:
        # Determine the largest square solar panel to allocate to the given area.
        square = int(math.pow(math.floor(math.sqrt(area)),2))

        # Add the current square to the list of squares.
        solar_panels.append(square)

        # Recursively identify remaining sqaure solar panels.
        solution(area-square, solar_panels)

    # Once the area has been populated with a square solar panel, return the list.
    return solar_panels


print(solution(12))
print(solution(15324))
print(solution(1))
print(solution(1000000))
print(solution(1000001234))
print(solution(-12))
print(solution(100041200546846348348684351633435334))