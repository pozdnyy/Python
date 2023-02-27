"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

import copy

class Matrix:
    def __init__(self, collect):
        self.collect = collect

    def __str__(self):
        s = ''
        for i in range(len(self.collect)):
            s = s + ' '.join(map(str, self.collect[i])) + '\n'
        return s

    def __add__(self, other):
        if len(self.collect) != len(other.collect):
            return 'Нельзя складывать матрицы разной размерности!'
        res = copy.deepcopy(self.collect)
        for i in range(len(self.collect)):
            for j in range(len(self.collect[i])):
                res[i][j] = self.collect[i][j] + \
                    other.collect[i][j]
        return Matrix(res)


array1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_array1 = Matrix(array1)
m_array2 = Matrix(array2)
print('Первая матрица')
print(m_array1)
print('Вторая матрица')
print(m_array2)
sum_matrix = m_array1 + m_array2
print('Cумма матриц')
print(sum_matrix)