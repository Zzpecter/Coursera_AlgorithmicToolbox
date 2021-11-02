# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021

def optimal_weigth(knapsack_capacity, bars):
    # build DP matrix
    w_matrix = [[0] * (knapsack_capacity + 1) for i in range(number_of_bars)]

    # Set initial values
    w_matrix[0] = [bars[0] if bars[0] <= j else 0 for j in range(knapsack_capacity + 1)]

    for row in range(1, len(w_matrix)):
        for col in range(1, len(w_matrix[row])):
            value = w_matrix[row - 1][col]
            if bars[row] <= col:
                val = (w_matrix[row - 1][col - bars[row]]) + bars[row]
                if value < val:
                    value = val
                    w_matrix[row][col] = value
                else:
                    w_matrix[row][col] = value
            else:
                w_matrix[row][col] = value
    return w_matrix[-1][-1]


if __name__ == '__main__':
    knapsack_capacity, number_of_bars = map(int, input().split())
    bars = list(map(int, input().split()))

    print(optimal_weigth(knapsack_capacity, bars))
