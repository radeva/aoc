"""Advent of code 2022 - Day 2"""

INPUT_FILE = "input.txt"

ROCK = ['A', 'X']
PAPER = ['B', 'Y']
SCISSORS = ['C', 'Z']

SCORES = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3  # Scissors
}

ROUND_SCORES = {
    'WIN': 6,
    'DRAW': 3,
    'LOSE': 0
}

def get_my_round_score(round_choices):
    """Get my score for the current round"""
    opponent = round_choices[0]
    me = round_choices[1]

    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    # rock - paper - I win
    # scissors - rock - I win
    # paper - scissors - I win

    my_score = 0
    if (opponent in ROCK and me in ROCK) or (opponent in SCISSORS and me in SCISSORS) or (opponent in PAPER and me in PAPER):
        my_score += ROUND_SCORES['DRAW']

    elif (opponent in ROCK and me in PAPER) or (opponent in SCISSORS and me in ROCK) or (opponent in PAPER and me in SCISSORS):
        my_score += ROUND_SCORES['WIN']

    my_score += SCORES[me]

    return my_score

def main():
    """main"""
    rounds_input = open(INPUT_FILE, "r", encoding="utf8")
    rounds = rounds_input.readlines()

    my_total_score = 0
    for current_round in rounds:
        round_choices = current_round.split()
        round_score = get_my_round_score(round_choices)
        my_total_score += round_score
    print("My total score is: " + str(my_total_score))

main()
