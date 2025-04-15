# первый способ
def bubble_sort_first_way(data):
    for last_index in range(len(data) - 1, 0, -1):
        flag = False
        for item_index in range(last_index):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                flag = True
        if not flag:
            break
    return data


# второй способ
def bubble_sort_second_way(data):
    last_index = len(data) - 1
    swapped = True
    while swapped:
        swapped = False
        for item_index in range(last_index):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                swapped = True
        last_index -= 1
    return data


arr = [200, 150, 0, 100, 50, 1, -50, -100, -150, 200]

print(bubble_sort_first_way(arr))
print(bubble_sort_second_way(arr))
