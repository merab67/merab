import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Запрашиваем две строки у пользователя
строка_1 = input("Введите первую строку: ")
строка_2 = input("Введите вторую строку: ")

# Производим конкатенацию строк
результат = строка_1 + строка_2

# Выводим результат
print(f"Результат конкатенации: {результат}")