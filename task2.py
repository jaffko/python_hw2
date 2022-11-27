# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывестив консоль сам список и сумму его элементов.


n = int(input('введите натуральное n: '))
n_list = [None] * n
for i in range(1, len(n_list) + 1):
    n_list[i-1] = (1 + 1 / i) ** i
list_sum = 0
for item in n_list:
    list_sum += item
print(*n_list, sep=', ')
print(list_sum)
