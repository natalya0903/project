import calendar
import locale

# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

locale.setlocale(locale.LC_ALL, 'ru_RU')

def quarter_of(month):
    quarters = {
        1: "первого",
        2: "второго",
        3: "третьего",
        4: "четвертого"
    }
    # for m in range(1, 13):
    quarter = (month - 1) // 3 + 1
    return quarters[quarter]

months = {}
for k, v in enumerate(calendar.month_name, start=0):
    months[k] = v

month = [2, 6, 11]

for m in month:
    print("месяц %d (%s) является частью %s квартала" % (m, months[m].strip().lower(), quarter_of(m)))