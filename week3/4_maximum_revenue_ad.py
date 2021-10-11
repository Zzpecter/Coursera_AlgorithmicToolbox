# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021
import sys

def max_dot_product(a, b, result):
    # max times max, throw them out of the list, call function again.
    if a:
        max_a, max_b = max(a), max(b)
        result += max_a * max_b
        a.pop(a.index(max_a))
        b.pop(b.index(max_b))
    else:
        return result
    return max_dot_product(a, b, result)


if __name__ == '__main__':
    _ = int(input())
    a, b = [], []

    line = input().split()
    for num in line:
        a.append(int(num))

    line = input().split()
    for num in line:
        b.append(int(num))

    print(max_dot_product(a, b, 0))