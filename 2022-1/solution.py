INPUT_FILE="input.txt"

def getCaloriesPerElf(lines):
    elfs_calories = []
    currentElfCalories = 0

    for l in lines:    
        l = l.strip()
        if len(l) > 0:
            currentElfCalories += int(l)
        else:
            elfs_calories.append(currentElfCalories)
            currentElfCalories = 0;

    elfs_calories.append(currentElfCalories)
    elfs_calories.sort(reverse=True)

    return elfs_calories

def getMaxCalories(lines):
    calories_per_elf=getCaloriesPerElf(lines)
    return calories_per_elf[0];

def getCaloriesOfTopThree(lines):
    calories_per_elf=getCaloriesPerElf(lines)
    calories_of_top_three = 0;

    for i in range(3):
        calories_of_top_three += calories_per_elf[i]
    return calories_of_top_three;

def main():
    input = open(INPUT_FILE, "r")
    lines = input.readlines()

    print("Elf with most calories has " + str(getMaxCalories(lines)) + " calories.\n")
    print("Top 3 elfs with most calories have " + str(getCaloriesOfTopThree(lines)) + " calories in total.") 

main()