def init_lists():
    with open('input', 'r') as file:
        for line in file:
            row_items = line.split(' ')       
            left_list.append(int(row_items[0].strip()))
            right_list.append(int(row_items[len(row_items) - 1].strip()))

    l = sorted(left_list)
    r = sorted(right_list)

    return (l, r)

def get_distance(left_list, right_list):
    distance = 0

    for i in range(len(left_list)):
        distance += abs(left_list[i] - right_list[i])

    return distance;

def get_similarity_score(left_list, right_list):
    similarity_score = 0

    for i in range(len(left_list)):
        similarity_score += left_list[i] * right_list.count(left_list[i])

    return similarity_score

left_list = []
right_list = []

(left_list, right_list) = init_lists()
print(get_distance(left_list, right_list))
print(get_similarity_score(left_list, right_list))
