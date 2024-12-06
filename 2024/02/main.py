def get_safe_reports_count(input_file, safe_check_function):
    safe_reports_count = 0
    with open(input_file, 'r') as file:
        for report in file:
            if safe_check_function(report):
                safe_reports_count += 1

    return safe_reports_count

def is_report_safe(report):
    if type(report) is str:
        levels = list(map(int, report.split(' ')))
    if type(report) is list:
        levels = report

    if len(levels) == 1:
        return True
    
    is_increasing = levels[0] < levels[1]
    
    for i in range(len(levels) - 1):
        distance = abs(levels[i] - levels[i+1])
        if (distance < 1 or distance > 3) or \
            (is_increasing and levels[i] > levels[i+1]) or \
            (not is_increasing and levels[i] < levels[i+1]):
            return False
        
    return True

def is_report_safe_with_problem_dampener(report):
    if is_report_safe(report):
        return True
    
    levels = list(map(int, report.split(' ')))    
    for i in range(len(levels)):
        modified_levels = [x for j,x in enumerate(levels) if j != i]
        if is_report_safe(modified_levels):
            return True

    return False

def test_is_report_safe():
    assert is_report_safe("7 6 4 2 1") == True
    assert is_report_safe("1 2 7 8 9") == False
    assert is_report_safe("9 7 6 2 1") == False
    assert is_report_safe("8 6 4 4 1") == False
    assert is_report_safe("1 3 6 7 9") == True

def test_is_report_safe_with_problem_dampener():
    assert is_report_safe_with_problem_dampener("7 6 4 2 1") == True
    assert is_report_safe_with_problem_dampener("1 2 7 8 9") == False
    assert is_report_safe_with_problem_dampener("9 7 6 2 1") == False
    assert is_report_safe_with_problem_dampener("1 3 2 4 5") == True
    assert is_report_safe_with_problem_dampener("8 6 4 4 1") == True
    assert is_report_safe_with_problem_dampener("1 3 6 7 9") == True

def test_get_safe_reports_count():
    assert get_safe_reports_count('test_input', is_report_safe) == 2
    assert get_safe_reports_count('test_input', is_report_safe_with_problem_dampener) == 4

def main():
    print(get_safe_reports_count('input', is_report_safe))
    print(get_safe_reports_count('input', is_report_safe_with_problem_dampener))

main()