"""Advent of code 2022 - Day 2"""

INPUT_FILE = "input.txt"

ROUND_SCORES = {
    'WIN': 6,
    'DRAW': 3,
    'LOSE': 0
}

def get_my_round_score_part_1(round_choices):
    """Get my score for the current round"""
    rock = ['A', 'X']
    paper = ['B', 'Y']
    scissors = ['C', 'Z']

    scores = {
        'X': 1, # Rock
        'Y': 2, # Paper
        'Z': 3  # Scissors
    }

    opponent = round_choices[0]
    me = round_choices[1]

    my_score = 0
    if (opponent in rock and me in rock) or (opponent in scissors and me in scissors) or (opponent in paper and me in paper):
        my_score += ROUND_SCORES['DRAW']

    elif (opponent in rock and me in paper) or (opponent in scissors and me in rock) or (opponent in paper and me in scissors):
        my_score += ROUND_SCORES['WIN']

    my_score += scores[me]

    return my_score

def get_my_round_score_part_2(round_choices):
    """Get my score for the current round if X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win"""

    scores = {
        'A': 1, # Rock
        'B': 2, # Paper
        'C': 3  # Scissors
    }

    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    defeat_matrix = {
        'A': 'C',
        'C': 'B',
        'B': 'A'
    }

    reverse_defeat_matrix = {
        'C': 'A',
        'B': 'C',
        'A': 'B'
    }

    opponent = round_choices[0]
    goal = round_choices[1]
    my_round = ''
    my_score = 0
    if goal == 'X':
        my_round = defeat_matrix[opponent]
        my_score += ROUND_SCORES['LOSE']
    elif goal == 'Y':
        my_round = opponent
        my_score += ROUND_SCORES['DRAW']
    elif goal == 'Z':
        my_round = reverse_defeat_matrix[opponent]
        my_score += ROUND_SCORES['WIN']

    my_score += scores[my_round]
    return my_score


def main():
    """main"""
    rounds_input = open(INPUT_FILE, "r", encoding="utf8")
    rounds = rounds_input.readlines()

    my_total_score_part_1 = 0
    my_total_score_part_2 = 0
    for current_round in rounds:
        round_choices = current_round.split()
        round_score_part_1 = get_my_round_score_part_1(round_choices)
        my_total_score_part_1 += round_score_part_1
        round_score_part_2 = get_my_round_score_part_2(round_choices)
        my_total_score_part_2 += round_score_part_2

    print("Part 1 - My total score is: " + str(my_total_score_part_1))
    print("Part 2 - My total score is: " + str(my_total_score_part_2))

main()
