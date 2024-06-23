#Задачи на циклы и оператор условия------
#----------------------------------------
'''
(!!!Подсказка на следующие 5 задач - превратите число в строку, а потом работайте с строкой)
Задача 6

Найти сумму цифр числа.

    Пример:

    254314

    Сумма цифр числа - 19(2+5+4+3+1+4)

'''

number = 254314
number_str = str(number)
sum_of_digits = 0
for digit in number_str:
    sum_of_digits += int(digit)
print(f"Сумма цифр числа {number} - {sum_of_digits} ({'+'.join(number_str)})")


'''
Задача 7

Найти произведение цифр числа.

    Пример:

    254314

    Произведение цифр числа - 480(2*5*4*3*1*4)
'''

number = 254314
number_str = str(number)
product_of_digits = 1
for digit in number_str:
    product_of_digits += int(digit)
print(f"Произведение цифр числа {number} - {product_of_digits} ({'*'.join(number_str)})")

'''
Задача 8

Пользователь должен ввести число. Ваш код должен дать ответ на вопрос: есть ли среди цифр числа 5?
Если есть, код должен вывексти "Цифра 5 есть в числе", в противном случае вывести: "Цифры 5 нет в числе".
'''

number = input("Введите число: ")
found_digit_5 = False
for digit in number:
    if digit == '5':
        found_digit_5 = True
        break
if found_digit_5:
    print("Цифра 5 есть в числе")
else:
    print("Цифры 5 нет в числе")

'''
Задача 9

Найти максимальную цифру в числе

Пример:

    354359688

    'Цифра - 9 максимальная в числе 354359688'
'''

number = input("Введите число: ")
max_digit = '0'
for digit in number:
    if digit > max_digit:
        max_digit = digit
print(f"Цифра - {max_digit} максимальная в числе {number}")

'''
Задача 10

Найти количество цифр 5 в числе

    Пример:

        543231235643

        'В числе 2 5-ки.'
'''

number = input("Введите число: ")
count_of_fives = 0
for digit in number:
    if digit == '5':
        count_of_fives += 1
print(f"В числе {count_of_fives} 5-ки.")
