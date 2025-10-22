def load_triangle(filename):
    with open(filename, 'r') as f:
        return [list(map(int, line.split())) for line in f]

def maximum_path_sum(triangle):
    # Start from the second last row and work our way upwards
    for row in range(len(triangle) - 2, -1, -1):  # from second last row to the first row
        for col in range(len(triangle[row])):
            # Replace the current element with the sum of the element and the max of the two adjacent elements in the row below
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
    # The top element will now contain the maximum total
    return triangle[0][0]

# Example of usage
if __name__ == "__main__":
    triangle = load_triangle("triangle.txt")  # Replace "triangle.txt" with your actual file path
    result = maximum_path_sum(triangle)
    print("The maximum total is:", result)
