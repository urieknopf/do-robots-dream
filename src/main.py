import sys
import pandas as pd
import numpy as np


def main():
    rows, columns, iterations = get_matrix_details()
    origin_matrix = pd.DataFrame(np.random.randint(0, 2, size=(int(rows), int(columns))))
    print("Original:\n", origin_matrix)
    final_matrix = evolve(origin_matrix, iterations)
    print("Final:\n", final_matrix)


def get_matrix_details():
    count = 1
    while count < 4:
        print("Please enter a integer values.")
        row_size = input("Enter number of rows: ")
        column_size = input("Enter number of columns: ")
        generations = input("\nEnter number of generations: ")
        try:
            row_size, column_size, generations = int(row_size), int(column_size), int(generations)
            return row_size, column_size, generations
        except ValueError:
            count += 1
    print("\n~* You have exhausted my patience. *~\n")
    return 0, 0, 0


def evolve(matrix, num_iterations):
    """ Evolves for a given number of iterations"""
    count = 1
    while count <= num_iterations:
        matrix = laws_of_nature(matrix)
        print(f"Iteration {count} of {num_iterations}\nmatrix")
        count += 1
    return matrix


def laws_of_nature(matrix):
    """Method to evolve the matrix on generation based on basic Conway evolution rules."""
    # check if cell survives and change to 0 if it doesn't
    # also check if dead cell is brought to life
    return matrix

if __name__ == '__main__':
    sys.exit(main())
