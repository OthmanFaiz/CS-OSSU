import math

def polysum(n,s):
    '''
    assumes n an int (number of sides)
    assumes s an int (length of the side)
    return sum the area and square of the perimeter of the "regular polygon" (rounded to 4 decimal places)
    '''

    # The area of regular polygon
    area = 0.25*n*s**2 / math.tan(math.pi/n)

    # The perimeter of a polygon
    perimeter = n * s

    # returing the sum and rounding to 4 decimal places.
    return round(area + perimeter **2, 4)

print(polysum(37, 61))