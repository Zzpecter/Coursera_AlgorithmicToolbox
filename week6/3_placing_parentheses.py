# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_min_max(i, j, op, min_values, max_values):
    lowest_min = 10000
    highest_max = -10000

    for k in range(i, j):
        a = evaluate(max_values[i][k], max_values[k + 1][j], op[k])
        b = evaluate(max_values[i][k], min_values[k + 1][j], op[k])
        c = evaluate(min_values[i][k], max_values[k + 1][j], op[k])
        d = evaluate(min_values[i][k], min_values[k + 1][j], op[k])

        lowest_min = min(lowest_min, a, b, c, d)
        highest_max = max(highest_max, a, b, c, d)

    return lowest_min, highest_max


def get_maximum_value(dataset):
    op = dataset[1:len(dataset):2]
    d = dataset[0:len(dataset) + 1:2]
    n = len(d)

    min_values = [[0 for i in range(n)] for j in range(n)]
    max_values = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        min_values[i][i] = int(d[i])
        max_values[i][i] = int(d[i])

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_values[i][j], max_values[i][j] = get_min_max(i, j, op, min_values, max_values)
    return max_values[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
