# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

def gcd_rene(a, b):
    if b != 0:
        a_prime = a % b
        return gcd_rene(b, a_prime)
    else:
        return a


if __name__ == "__main__":
    input = input()
    a, b = map(int, input.split())
    print(gcd_rene(a, b))