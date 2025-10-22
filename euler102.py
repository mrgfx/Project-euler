def area_of_triangle(x1, y1, x2, y2, x3, y3):
    # Area using the determinant method
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0

def is_origin_inside_triangle(x1, y1, x2, y2, x3, y3):
    # Area of the main triangle
    area_main = area_of_triangle(x1, y1, x2, y2, x3, y3)
    
    # Area of sub-triangles formed with the origin
    area1 = area_of_triangle(0, 0, x2, y2, x3, y3)
    area2 = area_of_triangle(x1, y1, 0, 0, x3, y3)
    area3 = area_of_triangle(x1, y1, x2, y2, 0, 0)
    
    # If the sum of the sub-triangle areas is equal to the area of the original triangle, the origin is inside
    return area_main == (area1 + area2 + area3)

def count_triangles_containing_origin(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Read the coordinates of the triangle
            coords = list(map(int, line.strip().split(',')))
            x1, y1, x2, y2, x3, y3 = coords
            
            # Check if the origin is inside the triangle
            if is_origin_inside_triangle(x1, y1, x2, y2, x3, y3):
                count += 1
    
    return count

# Usage example:
file_path = 'triangles.txt'
result = count_triangles_containing_origin(file_path)
print(f"Number of triangles containing the origin: {result}")
