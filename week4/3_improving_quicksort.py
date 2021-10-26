# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021
import random


def partition3(a, l, r):
    x = a[l]
    m_one = l  # index until which there are only numbers lower than X.
    m_two = l  # index until which there are only numbers equal to X.
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m_one += 1
            m_two += 1
            a[i], a[m_one] = a[m_one], a[i]
        elif a[i] == x:
            m_two += 1
            a[i], a[m_two] = a[m_two], a[i]
    a[l], a[m_one] = a[m_one], a[l]
    return m_one, m_two


def quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    m_one, m_two = partition3(a, l, r)
    # m = partition2(a, l, r)
    quick_sort(a, l, m_one - 1)
    quick_sort(a, m_two + 1, r)

    return a


if __name__ == '__main__':
    n = int(input())
    input= input()
    numbers = map(int, input.split())
    # numbers = [4, 9, 4, 9, 1]
    # n = 5

    numbers = quick_sort(numbers, 0, n - 1)
    for x in numbers:
        print(x, end=' ')
