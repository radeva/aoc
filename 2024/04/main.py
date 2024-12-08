import re

def read_input(file_input):
    lines = []
    with open(file_input, 'r') as file:
        for line in file:
            lines.append(line.strip('\n'))

    return lines

def get_matrix(lines):
    matrix = []
    for l in lines:
       matrix.append(list(l))

    return matrix 

def get_reversed_matrix(lines):
    matrix = get_matrix(lines)
    reversed_matrix = []

    for j in range(len(matrix[0])):
        reversed_matrix.append([])
        for i in range(len(matrix)):
            reversed_matrix[j].append(matrix[i][j])

    return reversed_matrix

def get_horizontal_count(lines):
    total_count = 0
    for l in lines:
      total_count += sum(1 for _ in re.finditer('(?=XMAS)', l))
      total_count += sum(1 for _ in re.finditer('(?=SAMX)', l))

    return total_count

def get_vertical_count(lines):
    reversed_matrix = get_reversed_matrix(lines)
    columns = []
    for i in range(len(reversed_matrix)):
        columns.append(''.join(reversed_matrix[i]))

    return get_horizontal_count(columns)

def get_diagonals_top_right(matrix):
    diagonals = []
    start_column = 0
    rows_count = len(matrix)
    columns_count = len(matrix[0])

    while start_column < columns_count:
        current_diagonal = ''
        for i in range(rows_count):
            if (i+start_column) < columns_count:
                current_diagonal += matrix[i][i+start_column]

        
        diagonals.append(current_diagonal)
        start_column += 1
    
    return diagonals

def get_diagonals_bottom_left(matrix):
    diagonals = []
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    start_row = 1
    while start_row < rows_count:
        current_diagonal = ''
        for i in range(columns_count):
            if (i+start_row) < rows_count:
                current_diagonal += matrix[i+start_row][i]

        diagonals.append(current_diagonal)
        start_row += 1

    return diagonals

def get_diagonals_count_left_to_right(lines):
    matrix = get_matrix(lines)
    diagonals = []

    diagonals += get_diagonals_top_right(matrix)
    diagonals += get_diagonals_bottom_left(matrix)

    return diagonals

def get_diagonals_count(lines):
    diagonals = []
    diagonals += get_diagonals_count_left_to_right(lines)

    reversed_lines = []
    for l in lines:
        reversed_lines.append(l[::-1])

    diagonals += get_diagonals_count_left_to_right(reversed_lines)

    return get_horizontal_count(diagonals)

def main():
    lines = read_input('./input/input')

    horizontal_count = get_horizontal_count(lines)
    vertical_count = get_vertical_count(lines)
    diagonals_count = get_diagonals_count(lines)

    total_count = horizontal_count + vertical_count + diagonals_count
    print(total_count)

main()