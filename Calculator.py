# переменные для ввода чисел a и b
a = float(input("Введите первое число: a = "))
b = float(input("Введите второе число: b = "))

# вычисляем сумму, разность, произведение, и проверяем деление на ноль для остальных операций
сумма = a + b
разность = a - b
произведение = a * b

# Проверяем, если b равно 0, то деление не выполняется
if b != 0:
    частное = a / b
    остаток = a % b
    целочисленное_деление = a // b
else:
    частное = "Деление на ноль невозможно"
    остаток = "Остаток от деления на ноль невозможен"
    целочисленное_деление = "Целочисленное деление на ноль невозможно"

возведение_в_степень = a ** b

# выводим результаты
print(f"Сумма a+b = {сумма}")
print(f"Разность a-b = {разность}")
print(f"Произведение a*b = {произведение}")
print(f"Частное a/b = {частное}")
print(f"Остаток от деления a%b = {остаток}")
print(f"Целочисленное деление a//b = {целочисленное_деление}")
print(f"Возведение в степень a**b = {возведение_в_степень}")




