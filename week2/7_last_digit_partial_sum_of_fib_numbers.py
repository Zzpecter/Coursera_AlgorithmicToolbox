# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def sum_iterative_fibonacci(last, actual, from_, until):
    actual_sum = last + actual
    for _ in range(from_, until):
        last, actual = actual, last + actual
        actual_sum += actual

    return actual_sum


def fibonacci(n):
    pair = True if n % 2 == 0 else False

    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    k = int(n/2 if pair else (n+1)/2)

    fib_k = fibonacci(k)
    fib_k_minus_1 = fibonacci(k - 1)

    fib_n = (2*fib_k_minus_1 + fib_k)*fib_k if pair else fib_k**2 + fib_k_minus_1**2

    return fib_n


if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    print((fibonacci(to + 2) - fibonacci(from_ + 1)) % 10)
