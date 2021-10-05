# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

def calc_fib(n):
    fib_map = [0, 1]
    index = 1

    if n == 0:
        return 0

    for _ in range(n-2):
        fib_map.append((fib_map[index-1] + fib_map[index]))
        index += 1
    return fib_map[index] + fib_map[index-1]

n = int(input())
print(calc_fib(n))