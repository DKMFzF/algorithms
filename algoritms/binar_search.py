wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]
my_ticket = 4567890


# первый способ
def binary_search(search_array, search_number):
    left = 0
    right = len(search_array) - 1
    while left <= right:
        mid = (left + right) // 2
        if search_array[mid] == search_number:
            return mid
        if search_array[mid] < search_number:
            left = mid + 1
        else:
            right = mid - 1
    return None


# второй способ
def find_element(sorted_numbers, target):
    left = 0
    right = len(sorted_numbers)

    while left < right:
        mid = (left + right) // 2
        if sorted_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid

    if left < len(sorted_numbers) and sorted_numbers[left] == target:
        return left
    return None


print(binary_search(wins, my_ticket))
