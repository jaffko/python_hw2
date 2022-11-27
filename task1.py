# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # 6782 -> 23
# # 0,56 -> 11

num = input('введите число: ')
if len(num.split('.')) == 1:
    num_list = num.split(',')
else:
    num_list = num.split('.')
digit_sum = 0
for i in range(len(num_list)):
    while int(num_list[i]) // 10 != 0:
        digit_sum += int(num_list[i]) % 10
        num_list[i] = int(num_list[i]) // 10
    digit_sum += int(num_list[i])
print(digit_sum)
