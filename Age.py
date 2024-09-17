# Переменные для хранения имени и возраста
имя = input("Введите ваше имя: ")  # Ввод имени
возраст = int(input("Введите ваш возраст в годах: "))  # Ввод возраста (в годах)

# Преобразование возраста в дни, часы и минуты
дней = возраст * 365  # Умножаем возраст на 365 дней в году
часов = дней * 24  # Умножаем дни на 24 часа
минут = часов * 60  # Умножаем часы на 60 минут

# Вывод приветствия и возраста с преобразованием
приветствие = f"Привет, {имя}! Тебе {возраст} лет!"
дополнительно = f"Это {дней} дней, или {часов} часов, или {минут} минут!"
print(приветствие)  # Вывод приветствия
print(дополнительно)  # Вывод дней, часов и минут