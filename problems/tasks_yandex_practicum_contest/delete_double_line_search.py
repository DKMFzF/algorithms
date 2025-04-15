# на вход поступает массив и длина массива
# удалить все повторения и заменить их на нижнее подчеркивание

# 3
# 1 1 2
# ответ -> 1 2 _

# 5
# 0 3 5 11 11
# ответ -> 0 3 5 11 _

# 10
# 0 0 1 1 1 2 2 3 3 4
# 0 1 2 3 4 _ _ _ _ _ _

len_arr = int(input())
input_arr = input().split()

clone_input_arr = []

input_arr_enumerate = enumerate(input_arr)

for item in input_arr_enumerate:
    if item[1] not in clone_input_arr:
        clone_input_arr.append(item[1])
        continue
    else:
        input_arr[item[0]] = '_'

for counter in range(len_arr + 1):
    if counter > len(clone_input_arr):
        clone_input_arr.append('_')

print(clone_input_arr)
