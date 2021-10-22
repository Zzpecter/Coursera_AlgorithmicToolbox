# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def get_majority_element(a, n):
    key_map = dict.fromkeys(set(a), 0)
    for element in a:
        key_map[element] = key_map[element] + 1

    for keys, values in key_map.items():
        if values > n/2:
            return 1
    return 0

if __name__ == '__main__':
    n = 4
    a = [1, 2, 3, 1]
    print(get_majority_element(a, n))