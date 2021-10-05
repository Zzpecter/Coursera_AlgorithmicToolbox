# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021
import sys


def lcm_rene(a, b):
    # used the formula: lcm(a,b) = |ab|/gcd(a,b)
    return int((a*b)/gcd_rene(a, b)) if a != 0 and b != 0 else 0


# from last exercise
def gcd_rene(a, b):
    if b != 0:
        a_prime = a % b
        return gcd_rene(b, a_prime)
    else:
        return a

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_rene(a, b))

