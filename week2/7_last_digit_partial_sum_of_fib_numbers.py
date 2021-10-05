# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

global fib_map


def sum_iterative_fibonacci(last, actual, from_, until):
    actual_sum = 0
    for _ in range(from_, until+1):
        actual_sum += actual
        last, actual = actual, last + actual

    return actual_sum


def fibonacci(n):
    pair = True if n % 2 == 0 else False

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        fib_map[n] = 1
        return fib_map[n]

    if fib_map[n] != 0:
        return fib_map[n]

    k = int(n/2 if pair else (n+1)/2)

    fib_k = fibonacci(k)
    fib_k_minus_1 = fibonacci(k - 1)

    fib_map[n] = (2*fib_k_minus_1 + fib_k)*fib_k if pair else fib_k**2 + fib_k_minus_1**2

    return fib_map[n]


def get_partial_fib_sum(n, m):
    actual = fibonacci(n)
    last = fibonacci(n-1)
    return sum_iterative_fibonacci(last, actual, n, m)


def get_last_digit(d):
    return int(str(d)[-1:])


if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    fib_map = [0] * (to + 3)
    print(get_last_digit(get_partial_fib_sum(from_, to)))