"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""

from timeit import timeit, default_timer
enter_n = int(input("Введите натуральное число: "))


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    revers_num = reversed(str(enter_num))
    return revers_num


def revers_5(enter_num, revers_num=''):
    revers_num += enter_num % 10
    enter_num //= 10
    if enter_num == 0:
        return revers_num
    return revers_5(enter_num, revers_num)


print(
    timeit(
        "revers(enter_n, revers_num=0)",
        setup='from __main__ import revers, enter_n',
        number=10000))

print(
    timeit(
        "revers_2(enter_n, revers_num=0)",
        setup='from __main__ import revers_2, enter_n',
        number=10000))

print(
    timeit(
        "revers_3(enter_n)",
        setup='from __main__ import revers_3, enter_n',
        number=10000))

print(
    timeit(
        "revers_4(enter_n)",
        setup='from __main__ import revers_4, enter_n',
        number=10000))

print(
    timeit(
        "revers_5(enter_n, revers_num=0)",
        setup='from __main__ import revers_5, enter_n',
        number=10000))
##############################################################
# Места по скорости выполнения кода:
# 1е встроенная функция reversed() и срез строки [::-1] - нет перебора по элементам
# 2е рекурсия и цикл while, отстают более чем на 1 порядок от 1го места - присутствует перебор по эл-ам, время выполнения кода увеличивается
# 3е место оператор ветвления if else, самое медленное выполнение кода - присутствует перебор по эл-ам,
# время выполнения кода увеличивается, плюс при каждом проходе сравнивание с 0 в новом цикле