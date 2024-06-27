#!/usr/bin/python3
"""
Defines function to calculate the perimeter of the island
represented by a list of list of integers.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island represented by the grid.

    grid [list of list of ints]: A list of list of integers representing the island and surrounding water.
        * 0s represent water and 1s represent land.
        * Each cell is a square with side length of 1.
        * Cells are connected horizontally/vertically (not diagonally).
        * Grid is rectangular, with width and height not exceeding 100.
        * The grid is entirely surrounded by water.
        * The island does not have "lakes" (water completely inside the island).
        * There is only one island or nothing.
    
    Returns:
        The perimeter of the island.

    Raises:
        TypeError: If grid is not a list of lists of integers.
        ValueError: If grid contains values other than 0 and 1.
    """
    # Validate the input
    error_msg = "grid must be a list of lists of integers"
    if type(grid) is not list:
        raise TypeError(error_msg)
    for row in grid:
        if type(row) is not list:
            raise TypeError(error_msg)
        for column in row:
            if type(column) is not int:
                raise TypeError(error_msg)
            if column not in [0, 1]:
                raise ValueError("grid must contain only 0s and 1s representing water and land")
    
    perimeter = 0
    # Iterate through each cell in the grid
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                # If the cell is land, check its edges
                perimeter += is_edge(grid, row, column)
    return perimeter

def is_edge(grid, row, column):
    """
    Determines if the given cell is on the edge of the island.

    Returns:
        1-4: If the given cell is on an edge, the number of edges.
        0: If the cell of land is in the interior of the island.
    """
    edge_count = 0
    if row == 0 or grid[row - 1][column] == 0:
        edge_count += 1  # Check the upper edge
    if row == len(grid) - 1 or grid[row + 1][column] == 0:
        edge_count += 1  # Check the lower edge
    if column == 0 or grid[row][column - 1] == 0:
        edge_count += 1  # Check the left edge
    if column == len(grid[row]) - 1 or grid[row][column + 1] == 0:
        edge_count += 1  # Check the right edge
    return edge_count

# Test the function with the provided grid
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Expected output: 12

