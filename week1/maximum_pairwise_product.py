import random


def pythonic_max_pairwise_product(numbers):
    first = numbers.pop(numbers.index(max(numbers)))
    return first*numbers.pop(numbers.index(max(numbers)))


def max_pairwise_product(numbers):
    first = 0
    second = 0
    for number in numbers:
        if number > first and number > second:
            second = first
            first = number
        elif first >= number > second:
            second = number

    return first*second


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    # tests = 500

    # for n in range(tests):
    #     input_n = random.randint(2, 50)
    #     numbers = [random.randint(2, 10000) for _ in range(input_n)]
    #     print(f'generated input: {numbers}')
    #
    #     normal_result = max_pairwise_product(numbers)
    #     pythonic_result = pythonic_max_pairwise_product(numbers)
    #
    #     print(f'max pairwise product: {normal_result}')
    #     print(f'pythonic max pairwise product: {pythonic_result}')
    #     print('OK') if pythonic_result == normal_result else print('FAIL')
    print(max_pairwise_product(input_numbers))