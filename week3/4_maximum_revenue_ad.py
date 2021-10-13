# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021
import sys

def get_negative_pairs(a, b):
    # count negatives on both lists
    a_negs = 0
    for num in reversed(a):
        if num < 0:
            a_negs += 1
        else:
            break

    b_negs = 0
    for num in reversed(b):
        if num < 0:
            b_negs += 1
        else:
            break

    # the lowest pairs get converted to their absolute value
    for index in range(min(a_negs, b_negs)):
        a[-index] = abs(a[-index])

    return a, b


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
    a = sorted(a)

    line = input().split()
    for num in line:
        b.append(int(num))
    b = sorted(b)

    a, b = get_negative_pairs(a, b)


    print(max_dot_product(a, b, 0))