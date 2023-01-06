# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def list_rand_nums(count):
    if count < 0:
        print("negative value")
    return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums

def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for a in range(len_list // 2):
        res_list.append(list_nums[a] * list_nums[len_list - a - 1])
        
    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list

all_list = list_rand_nums(int(input("number: ")))
print(all_list)
print(prod_pairs(all_list))
