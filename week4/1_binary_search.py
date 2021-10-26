# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

def binary_search(input_list, target_value):
    min_index = 0
    max_index = len(input_list) - 1

    try:
        return input_list.index(target_value)
    except ValueError:
        return -1

    # while max_index >= min_index:
    #     mid_index = (max_index+min_index) // 2
    #     if input_list[mid_index] == target_value:
    #         while mid_index > 0 and input_list[mid_index - 1] == input_list[mid_index]:
    #             mid_index -= 1
    #         return input_list.index(target_value)
    #     elif input_list[mid_index] < target_value:
    #         min_index = mid_index+1
    #     else:
    #         max_index = mid_index-1
    # return -1

if __name__ == '__main__':
    _ = input()
    input_keys = list(map(int, input().split()))
    _ = input()
    input_queries = list(map(int, input().split()))
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
