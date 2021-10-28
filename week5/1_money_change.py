# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

DENOMINATIONS = [0, 1, 3, 4]
INF = 100000


def coin_change(n):
    num_denominations = len(DENOMINATIONS) - 1
    coins_to_use = [0]*(n+1)

    for j in range(1, n+1):
        minimum = INF

        for i in range(1, num_denominations+1):
            if j >= DENOMINATIONS[i]:
                minimum = min([minimum, 1+coins_to_use[j-DENOMINATIONS[i]]])
        coins_to_use[j] = minimum
    return coins_to_use[n]

if __name__ == '__main__':
    m = int(input())
    print(coin_change(m))
