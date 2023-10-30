import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Args:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    area = math.pi * radius ** 2
    return area

# Example usage:
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print("The area of the circle is: {:.2f}".format(area))
