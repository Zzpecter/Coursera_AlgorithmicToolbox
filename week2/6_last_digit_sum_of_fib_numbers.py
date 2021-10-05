# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

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


def get_sum(n):
    return (fibonacci(n + 2) - 1)


def get_last_digit_of_sum(n):
    return int(str(get_sum(n))[-1:])


if __name__ == '__main__':
    n = int(input())
    print(get_last_digit_of_sum(n))
