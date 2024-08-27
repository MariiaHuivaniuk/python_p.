def binary_search(sorted_list, item):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        number = sorted_list[mid]

        if number == item:
            return mid
        elif number < item:
            low = mid + 1
        else:
            high = mid - 1

    return None
sorted_list = list(range(1, 100))
item = 48

index = binary_search(sorted_list, item)

if index is not None:
    print(f"Елемент {item} знайдено в позиції {index}")
else:
    print(f"Елемент {item} не знайдено в списку")
