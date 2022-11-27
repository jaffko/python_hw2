# # Написать программу, которая состоит 4 из этапов:
# # - создает список из рандомных четырех значных чисел
# # - принимает с консоли цифру и удаляет ее из всех элементов списка
# # - цифры каждого элемента суммирует пока результат не станет однозначным числом
# # - из финального списка убирает все дублирующиеся элементы
# # - после каждого этапа выводить результат в консоль
# # Пример:
# # - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# # - 2 этап: Введите цифру: 3
# # - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# # - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# # - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# # - 4 этап: [3, 1, 5, 4]

from random import randint as rnd

size = int(input('введите размерность массива: '))
numbers_list = [rnd(1000, 9999) for _ in range(size)]
print(f'1 этап: {numbers_list}')
num_to_delete = input('введите цифру для удаления: ')
for i in range(size):
    numbers_list[i] = str(numbers_list[i])
    reduced = 0
    for j in range(4):
        if numbers_list[i][j - reduced] == num_to_delete:
            if j == 3:
                numbers_list[i] = numbers_list[i][:j - reduced]
            else:
                numbers_list[i] = numbers_list[i][:j - reduced] + numbers_list[i][j - reduced + 1:]
                reduced += 1
    numbers_list[i] = int(numbers_list[i])
print(f'2 этап: {numbers_list}')
# for i in range(size):
#     numbers_list[i] = str(numbers_list[i])
#     number_sum = 0
#     while int(numbers_list[i]) // 10 != 0:
#         for j in range(len(str(numbers_list[i]))):
#             number_sum += int(numbers_list[i][j])
#         numbers_list[i] = number_sum
#     numbers_list[i] = int(numbers_list[i])
# print(f'3 этап: {numbers_list}')
# это еще не работает.......

