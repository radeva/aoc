"""Advent of code 2022 - Day 6"""

INPUT_FILE = "input.txt"

def get_processed_characters(signals, number_of_characters_marker):
    """Get characters that need to be processed before the first start-of-packet marker is detected """
    for i in range(0,len(signals)-number_of_characters_marker):
        current_marker = signals[i:i+number_of_characters_marker]
        if len(set(current_marker)) == number_of_characters_marker:
            return i+number_of_characters_marker

def test_get_processed_characters():
    """Test get_processed_characters"""
    assert get_processed_characters("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4) == 7
    assert get_processed_characters("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert get_processed_characters("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert get_processed_characters("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert get_processed_characters("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11

    assert get_processed_characters("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert get_processed_characters("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert get_processed_characters("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert get_processed_characters("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert get_processed_characters("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

def main():
    """main"""
    task_input = open(INPUT_FILE, "r", encoding="utf8")
    lines = task_input.readlines()
    signals = lines[0].rstrip('\n')
    processed_characters = get_processed_characters(signals, 4)
    print("Part 1: Start marker characters to be processed are " + str(processed_characters))

    processed_characters = get_processed_characters(signals, 14)
    print("Part 2: Message marker characters to be processed are " + str(processed_characters))

main()
