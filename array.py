# Array in python
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr)

# Mendefinisikan default value
var_arr = [0 for i in range(10)]

for i in range(10):
    var_arr[i] = i

print(var_arr)

# How to access the element of array
var_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(var_arr[0])


# pemrosesan sekuensial pada array
var_arr = [1, 2, 3, 4, 5]
for i in range(len(var_arr)):
    current_element = var_arr[i]
    next_index = i + 1

    if next_index < len(var_arr):
        next_element = var_arr[next_index]
    else:
        next_element = None

    print(f"Current element: {current_element}, next elements: {next_element}")

'''
Pointer "left": berada pada indekx pertama dan menyatakan bahwa pointer "left" selalu menunjukkan nilai terbesar dalam array
Pointer "right": akan selalu berada pada elemen selanjutnya dan membandingkannya dengan element pointer left
'''
var_arr = [1,7,2,89,3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)