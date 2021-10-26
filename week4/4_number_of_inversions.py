# Created by: René Vilar S.
# Algorithmic Toolbox - Coursera 2021


def merge_sort(arr, n):
    temp_arr = [0] * n
    return get_number_of_inversions(arr, temp_arr, 0, n - 1)


def get_number_of_inversions(arr, temp_arr, left, right):

    inversion_counter = 0

    if left < right:
        mid = (left + right) // 2

        inversion_counter += get_number_of_inversions(arr, temp_arr, left, mid)
        inversion_counter += get_number_of_inversions(arr, temp_arr, mid + 1, right)
        inversion_counter += merge(arr, temp_arr, left, mid, right)
        
    return inversion_counter


def merge(arr, temp_arr, left, mid, right):
    i = left  
    j = mid + 1  
    k = left  
    inversion_counter = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inversion_counter += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inversion_counter


if __name__ == '__main__':
    # input = input()
    # n, *a = list(map(int, input.split()))
    a = [2, 3, 9, 2, 9]
    n= len(a)
    b = n * [0]
    print(merge_sort(a, n))
