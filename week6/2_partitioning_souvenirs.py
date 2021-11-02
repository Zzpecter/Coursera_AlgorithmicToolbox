# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def partition(souvenirs):

    total = sum(souvenirs)
    if len(souvenirs) < 3 or total % 3:  # 1
        return False
    third = total // 3
    table = [[0] * (len(souvenirs) + 1) for _ in range(third + 1)]  # 2

    for i in range(1, third + 1):
        for j in range(1, len(souvenirs) + 1):  # 3
            ii = i - souvenirs[j - 1]  # 4
            if souvenirs[j - 1] == i or (ii > 0 and table[ii][j - 1]):  # 5
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]  # 6

    return 1 if table[-1][-1] == 2 else 0

if __name__ == '__main__':
    _ = input()
    souvenirs = list(map(int, input().split()))
    print(partition(souvenirs))
