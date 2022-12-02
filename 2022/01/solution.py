"""Advent of code 2022 - Day 1"""

INPUT_FILE = "input.txt"

def get_calories_per_elf(lines):
    """Find how many calories each elf is bringing"""
    elfs_calories = []
    current_elf_calories = 0

    for line in lines:    
        line = line.strip()
        if len(line) > 0:
            current_elf_calories += int(line)
        else:
            elfs_calories.append(current_elf_calories)
            current_elf_calories = 0

    elfs_calories.append(current_elf_calories)
    elfs_calories.sort(reverse=True)

    return elfs_calories

def main():
    """main"""
    task_input = open(INPUT_FILE, "r", encoding="utf8")
    lines = task_input.readlines()

    calories_per_elf = get_calories_per_elf(lines)
    max_calories = calories_per_elf[0]
    calories_of_top_three = sum(calories_per_elf[0:3])

    print("Elf with most calories has " + str(max_calories) + " calories.")
    print("Top 3 elfs with most calories have " + 
        str(calories_of_top_three) + " calories in total.")

main()
