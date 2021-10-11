# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

DENOMINATIONS = [10, 5, 1]

def get_change(m):
    num_coins = 0

    for denomination in DENOMINATIONS:
        while m >= denomination:
            m -= denomination
            num_coins += 1
        if m == 0:
            break
    return num_coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))