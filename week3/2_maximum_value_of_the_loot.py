# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def get_optimal_value(capacity, weights, values):

    value_to_weight_ratios = [value/weight for weight, value in zip(weights, values)]
    total_value = 0

    while capacity > 0:
        max_index = value_to_weight_ratios.index(max(value_to_weight_ratios))

        if capacity >= weights[max_index]:
            # take all
            # reduce the inventory capacity
            capacity -= weights[max_index]

            # increase total value gained
            total_value += values[max_index]

            # reduce weight from the stack to 0
            weights[max_index] = 0

            # reduce value_to_weight_ratios from the stack to 0
            value_to_weight_ratios[max_index] = 0

        else:
            # take to fill
            # increase total value gained
            total_value += values[max_index] * capacity / weights[max_index]

            # reduce the inventory capacity
            capacity = 0

            # reduce weight from the stack
            weights[max_index] -= capacity
    return total_value


if __name__ == "__main__":
    weights, values = [], []

    # input parsing
    line = input().split()
    num_lines_to_come = int(line[0])
    capacity = int(line[1])

    for _ in range(num_lines_to_come):
        line = input().split()
        values.append(int(line[0]))
        weights.append(int(line[1]))

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.8f}".format(opt_value))
