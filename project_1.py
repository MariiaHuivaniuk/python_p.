def insertion_sort(arr):
    for i in range(len(arr)):
        current_value = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current_value
    return arr

numbers = [38, 54, 5, 9, 0, 10, 3, 77, 1, 95, 34, 99, 15]
sorted_numbers = insertion_sort(numbers)
print(f'Відсортований список: {sorted_numbers}')