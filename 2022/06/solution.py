"""Advent of code 2022 - Day 6"""

INPUT_FILE = "input.txt"

def get_processed_characters(signals):
    """Get characters that need to be processed before the first start-of-packet marker is detected """
    for i in range(0,len(signals)-4):
        current_marker = signals[i:i+4]
        if len(set(current_marker)) == 4:
            return i+4

def test_get_processed_characters():
    """Test get_processed_characters"""
    assert get_processed_characters("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert get_processed_characters("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert get_processed_characters("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert get_processed_characters("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert get_processed_characters("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

def main():
    """main"""
    task_input = open(INPUT_FILE, "r", encoding="utf8")
    lines = task_input.readlines()
    signals = lines[0].rstrip('\n')
    processed_characters = get_processed_characters(signals)
    print("Part 1: characters need to be processed are " + str(processed_characters))

main()
