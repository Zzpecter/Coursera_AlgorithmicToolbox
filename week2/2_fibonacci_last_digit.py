# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

def get_fibonacci_last_digit_rene(n):
    previous, current = 0, 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return int(str(current)[-1:])


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_rene(n))