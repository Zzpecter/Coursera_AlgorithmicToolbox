# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def get_fibonacci_pisano_rene(n):
    pisano_period = get_pisano_period(10)
    remainder_n = n % pisano_period

    previous, current = 0, 1
    for _ in range(remainder_n - 1):
        previous, current = current, previous + current

    return current


def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m ** 2):
        previous, current = current, (previous + current) % m

        # Pisano Period always starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def format_output(f_n, f_n_plus_1):
    return ((f_n % 10) * (f_n_plus_1 % 10)) % 10


if __name__ == '__main__':
    n = int(input())
    if n != 0:
        f_n = get_fibonacci_pisano_rene(n)
        f_n_plus_1 = get_fibonacci_pisano_rene(n+1)
        print(format_output(f_n, f_n_plus_1))
    else:
        print(0)
    # print(f'fib_n: {f_n} fib_n+1: {f_n_plus_1}')
    # print(f'mod_fib_n: {f_n%10} mod_fib_n+1: {f_n_plus_1%10}')
    # print(f'last digit: {((f_n%10) * (f_n_plus_1%10))%10}')
