#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей длиной 4, причем каждая строка должна быть пронумерована.

Пример:
    0 0000
    1 0000
    2 0000
    3 0000
....
'''

for i in range(1, 6):
    print(f"{i}: {'0' * 4}")

'''
Задача 2

Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
'''

count_of_fives = 0
for _ in range(10):
    digit = input("Введите цифру: ")    
    if digit.isdigit() and 0 <= int(digit) <= 9:
        if digit == '5':
            count_of_fives += 1
    else:
        print("Пожалуйста, введите одну цифру от 0 до 9.")
print(f"Количество введенных цифр 5: {count_of_fives}")

'''
Задача 3

Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

sum_series = 0
for i in range(1, 101):
    sum_series += i
print(f"Сумма ряда чисел от 1 до 100: {sum_series}")

'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).
'''

import math
n = 10
product_series = math.factorial(n)
print(f"Произведение ряда чисел от 1 до {n}: {product_series}")

'''
(!!!Подсказка на следующую задачу - превратите число в строку, а потом работайте с строкой)
Задача 5

Вывести цифры числа на каждой новой строке.

Пример:
     123567

     1
     2
     3
     4
     5
     6
     7

'''

number = input("Введите число: ")
for digit in number:
    print(digit)
     
    
    
    