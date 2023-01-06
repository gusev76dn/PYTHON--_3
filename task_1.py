# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample
def list_rand_nums(count: int) -> list:
    if count < 0:
        print("negative value")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums

def sum_odd_pos(list_nums: list):
    sum_nums = 0
    for a in range(0, len(list_nums), 2):
        sum_nums += list_nums[a]
        return sum_nums

all_list = list_rand_nums(int(input("namder: ")))
print(all_list)