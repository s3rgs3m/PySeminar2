"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

var1 = 7
var2 = "строка"
var3 = 3
print("var1:", var1, "type:", type(var1))
print("var2:", var2, "type:", type(var2))
print("var2:", var3, "type:", type(var3))
print(f'var1 + var3 = {var1+var3}')
user_var1 = input("Введите слово: ")
user_var2 = int(input("Введите целове число: "))
print(f'Вы ввели число {user_var2} и слово "{user_var1}"')