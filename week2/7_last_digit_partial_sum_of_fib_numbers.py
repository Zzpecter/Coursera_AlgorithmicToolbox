# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def get_fibonacci_rene(n):
    pisano_period = get_pisano_period(10)
    remainder_n = n % pisano_period

    if remainder_n == 0:
        return 0

    previous, current = 0, 1
    for _ in range(remainder_n - 1):
        previous, current = current, previous + current

    return current % 10


def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(m ** 2):
        previous, current = current, (previous + current) % m

        # Pisano Period always starts with 01
        if (previous == 0 and current == 1):
            return i + 1

if __name__ == '__main__':
    input = input()
    from_, to = map(int, input.split())
    print((get_fibonacci_rene(to + 2) - get_fibonacci_rene(from_ + 1)) % 10)
