# 1 3 5 6
# 5
# ответ 2

# 1 5 10 11
# 2
# ответ 2

# 3 7 10 20 23
# 25
# ответ 5

# 5 5 5 5
# 5

arr_input = input().split()
target = int(input())

done_arr = [int(x) for x in arr_input]


def search_concentration(search_arr, target):
    left = 0
    right = len(search_arr)
    while left < right:
        mid = (left + right) // 2
        if search_arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


print(search_concentration(done_arr, target))
