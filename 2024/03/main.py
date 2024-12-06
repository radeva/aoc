import re

def get_mul_instructions(input_file):
    with open(input_file, 'r') as file:
        all_mul_instructions = []
        for line in file:
            all_mul_instructions = all_mul_instructions + re.findall("mul\(\d{1,3}\,\d{1,3}\)", line)
   
    return all_mul_instructions

def get_sum_of_muls(mul_instructions):
    sum = 0
    for mi in mul_instructions:
        current_match = re.match("mul\((\d{1,3})\,(\d{1,3})\)", mi)
        sum += int(current_match.group(1)) * int(current_match.group(2))

    return sum

def main():
    mul_instructions = get_mul_instructions('input')
    print(get_sum_of_muls(mul_instructions))

main()