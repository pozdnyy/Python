"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker():

    def __init__(pers, lname, fname, job_title, salary, bonus):
        pers.lname = lname
        pers.fname = fname
        pers.job_title = job_title

        pers.salary = salary
        pers.bonus = bonus
        pers._income = {'salary': pers.salary, 'bonus':  pers.salary * pers.bonus / 100}

class Job_title(Worker):

    def get_full_name(pers):
        return pers.lname + ' ' + pers.fname

    def get_total_income(pers):
        return pers._income.get('salary') +  pers._income.get('bonus')

w1 = Job_title('Широков', 'Никита', 'сварщик', 1000, 25)
print('Имя:', w1.fname)
print('Фамилия:', w1.lname)
print('Должность:', w1.job_title)
print('Полное имя:', w1.get_full_name())
print('Оклад, руб.:', w1.salary)
print('Размер премии, %:', w1.bonus)
print('Размер дохода, руб.:', w1.get_total_income())

w2 = Job_title('Родин', 'Николай', 'моторист', 1200, 30)
print(w2.lname)
print(w2.fname)
print(w2.job_title)
print(w2.get_full_name())
print(w2.get_total_income())