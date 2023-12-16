
import math 

def calculate_house_square_footage(room_dimensions):
    total_square_footage = 0
    for length, width in room_dimensions:
        area = length * width
        total_square_footage += area

    return total_square_footage

room_dimensions = [
    (15, 12),  
    (10, 10),  
    (12, 10),  
    (10, 8)    
   
]

total_house_square_footage = calculate_house_square_footage(room_dimensions)
print(f"The total square footage of the house is: {total_house_square_footage} square feet")
 

def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = 5
circle_circumference = calculate_circle_circumference(radius)
print(f"The circumference of the circle with radius {radius} is: {circle_circumference:.2f} units")

