"""Advent of code 2022 - Day 3"""

INPUT_FILE = "input.txt"

def get_item_priority(char):
    """Get an item priority"""
    char_ascii = ord(char)
    if char_ascii >=97 and char_ascii <= 122:
        return char_ascii - 96

    if char_ascii >=65 and char_ascii <= 90:
        return char_ascii - 38

    raise Exception("Invalid character: " + char) 

def find_matching_item(racksack):
    """Find the matching item between the two compartments of a racksack"""
    racksack_length = len(racksack)
    racksack_midpoint = int(racksack_length / 2)

    left_compartment = set(racksack[0:racksack_midpoint])
    right_compartment = set(racksack[racksack_midpoint:racksack_length])

    return left_compartment.intersection(right_compartment).pop()

def find_matching_item_in_a_group(group):
    """Find matching item in a group"""
    group_sets = map(set, group)
    matching_item = set.intersection(*group_sets).pop()
    return matching_item

def main():
    """main"""
    racksacks_input = open(INPUT_FILE, "r", encoding="utf8")
    racksacks = racksacks_input.readlines()

    current_group = []
    total_priority = 0
    total_group_priority = 0
    for racksack in racksacks:
        racksack = racksack.rstrip('\n')
        ## Part 1
        total_priority += get_item_priority(find_matching_item(racksack))
        ## Part 2
        current_group.append(racksack)
        if len(current_group) == 3:
            total_group_priority += get_item_priority(find_matching_item_in_a_group(current_group))
            current_group = []

    print("Matching items total priority is " + str(total_priority))
    print("Groups matching items total priority is " + str(total_group_priority))

main()
