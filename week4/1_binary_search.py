# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def binary_search(keys, query, index_sum):
    mid_index = int(len(keys) / 2 if len(keys) % 2 == 0 else (len(keys) - 1) / 2)
    if keys[mid_index] != query:
        higher = True if query > keys[mid_index] else False

        if higher and mid_index != 0:
            index_sum += mid_index
            return binary_search(keys[mid_index:], query, index_sum)
        elif higher and mid_index == 0:
            return -1
        elif not higher and mid_index == 0 and index_sum == 0:
            return -1
        else:
            return binary_search(keys[:mid_index], query, index_sum)
    return index_sum + mid_index


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]
    for q in input_queries:
        print(binary_search(input_keys, q, 0), end=' ')