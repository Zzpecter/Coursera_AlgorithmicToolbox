# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

class Node:
    def __init__(self, value, root):
        self.value = value
        self.root = root

def divide_by_two(n):
    return n // 2 if n % 2 == 0 else None


def divide_by_three(n):
    return n // 3 if n % 3 == 0 else None


def subtract_one(n):
    return n - 1 if n > 1 else None


def optimal_sequence(n):
    actual_results = [n]
    new_results = []
    seen_numbers = {n}
    traceback_stack = [[]]  # TODO: find a way to trace

    while 1 not in actual_results:
        for number in actual_results:
            for op in OPERATIONS:
                res = op.__call__(number)
                if res and res not in seen_numbers:
                    seen_numbers.add(res)
                    new_results.append(res)
        actual_results = new_results
        new_results = []


OPERATIONS = [divide_by_two, divide_by_three, subtract_one]


if __name__ == '__main__':
    m = int(input())
    optimal_sequence(m)
