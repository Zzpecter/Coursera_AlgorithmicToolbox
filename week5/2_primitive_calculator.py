# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

def divide_by_two(n, step):
    if n % 2 == 0:
        NODE_DICT_LIST[step+1][n//2] = n
        return n//2
    return None


def divide_by_three(n, step):
    if n % 3 == 0:
        NODE_DICT_LIST[step+1][n//3] = n
        return n//3
    return None


def subtract_one(n, step):
    if n - 1 > 0:
        NODE_DICT_LIST[step+1][n-1] = n
        return n-1
    return None


def optimal_sequence(n):
    actual_results = [n]
    new_results = []
    seen_numbers = {n}
    steps = 0

    while 1 not in actual_results:
        for number in actual_results:
            for op in OPERATIONS:
                res = op.__call__(number, steps)
                if res and res not in seen_numbers:
                    seen_numbers.add(res)
                    new_results.append(res)
        actual_results = new_results
        new_results = []
        steps += 1
        NODE_DICT_LIST.append({})

    target_value = 1
    NODE_DICT_LIST.pop()  # empty dict
    step_list = [1]
    while 1:
        current_dict = NODE_DICT_LIST.pop()
        new_val = current_dict.get(target_value)
        if not new_val:
            break
        step_list.append(new_val)
        target_value = new_val

    return steps, step_list


OPERATIONS = [divide_by_two, divide_by_three, subtract_one]
NODE_DICT_LIST = [{100: None}, {}]


if __name__ == '__main__':
    m = int(input())
    steps, nums = optimal_sequence(m)
    print(steps)
    for n in nums:
        print(n, end=' ')
