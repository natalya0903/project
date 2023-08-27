import datetime
import calendar
import locale
from datetime import datetime
from calendar import monthrange

locale.setlocale(locale.LC_ALL, 'ru_RU')


# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

months = {}
for k, v in enumerate(calendar.month_name, start=0):
    months[k] = v
print('Введите номер месяца:')
month = int(input())
if month<=0 or month>12:
    print('Такого месяца нет!')
else:
    now_year = datetime.now().year
    d=calendar.monthrange(now_year, month)
    m=months[month].lower().strip()
    d=d[1]
    print('Вы ввели ', m, '. ', d, ' дней', sep='')