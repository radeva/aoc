INPUT_FILE="input.txt"

def getCaloriesPerElf(lines):
    elfs_calories = []
    current_elf_calories = 0

    for l in lines:    
        l = l.strip()
        if len(l) > 0:
            current_elf_calories += int(l)
        else:
            elfs_calories.append(current_elf_calories)
            current_elf_calories = 0;

    elfs_calories.append(current_elf_calories)
    elfs_calories.sort(reverse=True)

    return elfs_calories

def main():
    input = open(INPUT_FILE, "r")
    lines = input.readlines()

    calories_per_elf = getCaloriesPerElf(lines)
    max_calories = calories_per_elf[0]
    calories_of_top_three = sum(calories_per_elf[0:3])

    print("Elf with most calories has " + str(max_calories) + " calories.")
    print("Top 3 elfs with most calories have " + str(calories_of_top_three) + " calories in total.") 

main()