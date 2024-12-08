from main import *

def test_get_horizontal_count():
    lines = [
"MMMSXXMASM",
"MSAMXMSMSA",
"AMXSXMAAMM",
"MSAMASMSMX",
"XMASAMXAMM",
"XXAMMXXAMA",
"SMSMSASXSS",
"SAXAMASAAA",
"MAMMMXMMMM",
"MXMXAXMASX"
]

    assert get_horizontal_count(lines) == 5


def test_get_matrix():
    lines = read_input('./input/test_input')
    assert get_matrix(lines) == [
        ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], 
        ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], 
        ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'], 
        ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'], 
        ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], 
        ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'], 
        ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'], 
        ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'], 
        ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'], 
        ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
    
def test_get_reversed_matrix():
    lines = read_input('./test_input')
    assert get_reversed_matrix(lines) == [
        ['M', 'M', 'A', 'M', 'X', 'X', 'S', 'S', 'M', 'M'], 
        ['M', 'S', 'M', 'S', 'M', 'X', 'M', 'A', 'A', 'X'], 
        ['M', 'A', 'X', 'A', 'A', 'A', 'S', 'X', 'M', 'M'], 
        ['S', 'M', 'S', 'M', 'S', 'M', 'M', 'A', 'M', 'X'], 
        ['X', 'X', 'X', 'A', 'A', 'M', 'S', 'M', 'M', 'A'], 
        ['X', 'M', 'M', 'S', 'M', 'X', 'A', 'A', 'X', 'X'], 
        ['M', 'S', 'A', 'M', 'X', 'X', 'S', 'S', 'M', 'M'], 
        ['A', 'M', 'A', 'S', 'A', 'A', 'X', 'A', 'M', 'A'], 
        ['S', 'S', 'M', 'M', 'M', 'M', 'S', 'A', 'M', 'S'], 
        ['M', 'A', 'M', 'X', 'M', 'A', 'S', 'A', 'M', 'X']]
