# Ввод, вывод, комментарии---------
#----------------------------------


# однострочный комментарий

'''

первая строка
вторая строка
...

'''

# Вывод----------------------------
print('Hello!')
print('Hello!', 'Student!', 123)

print('Hello!', 'Student!', 123, sep = 'xxx')

print('Hello!', 'Student!', 123, end = 'yyy')

print()


# Ввод-----------------------------

age = input('Input your age')

print(age, type(age))
print(int(age), type(int(age)))