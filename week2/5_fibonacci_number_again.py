# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def get_fibonacci_modulo_rene(n, m):
    pisano_period = get_pisano_period(m)
    remainder_n = n % pisano_period

    if remainder_n == 0:
        return 0

    previous, current = 0, 1
    for _ in range(remainder_n - 1):
        previous, current = current, previous + current

    return current % m


def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(m ** 2):
        previous, current = current, (previous + current) % m

        # Pisano Period always starts with 01
        if (previous == 0 and current == 1):
            return i + 1

if __name__ == '__main__':
    input = input()
    n, m = map(int, input.split())

    print(get_fibonacci_modulo_rene(n, m))
