'''
Напишите функцию с двумя параметрами-строками. Функция возвращает булево значение True если вторая строка содержится
в первой строке как подстрока, и False в противном случае.
Например,
f("12345", "234") = True
f("12345", "235") = False
Для решения стандартные возможности типа s1 in s2 или слайсы или сравнения строк/списков (кроме посимвольного сравнения)
использовать нельзя, только условиями и циклами
'''


def f(s1, s2):
    if len(s2) == 0:  # пустая строка является подстройкой для любой другой
        return True
    j = 0
    for i in range(len(s1)):
        if s1[i] == s2[j]:
            j += 1
            if j == len(s2):
                return True
        else:
            j = 0
    return False

