# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

def calc_fib(n):
    fib_map = [0, 1]
    index = 1

    for _ in range(n-2):
        fib_map.append((fib_map[index-1] + fib_map[index]))
        index += 1
    print(fib_map)
    return fib_map[index]

n = int(input())
print(calc_fib(n))