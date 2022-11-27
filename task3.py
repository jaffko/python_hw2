# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint as rnd

size = int(input('введите размерность массива: '))
rnd_list = [rnd(0, 100) for i in range(size)]
print(rnd_list)
shuffle_list = [-1] * size
for i in range(size):
    rnd_index = rnd(0, size - 1)
    while shuffle_list[rnd_index] != -1:
        rnd_index = rnd(0, size - 1)
    shuffle_list[rnd_index] = rnd_list[i]
print(shuffle_list)


