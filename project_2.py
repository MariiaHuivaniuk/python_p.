def selection_sort(data):
    n = len(data)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if data[j][1] < data[min_index][1]:
                min_index = j

        data[min_index], data[i] = data[i], data[min_index]

    return data

data = [
    ("Python", 874),
    ("Django", 700),
    ("Макроекономіка", 91),
    ("Економетрика", 160),
    ("Іноземна мова", 64),
    ("Програмне забезпечення", 231),
    ("ООП", 175),
    ("Кібербезпека", 137),
    ("Маркетинг", 230)
]

sorted_data = selection_sort(data)

for item in sorted_data:
    print(f"{item[0]} - {item[1]}")