# 4 Задание
euro = float(input("Введите курс евро: "))
dollar = float(input("Введите курс доллара: "))
rubles = float(input("Введите сумму в рублях: "))
currency = input("Введите валюту для конвертации (доллары/евро): ")

if currency == 'доллары':
        converted = rubles / dollar
        print(f"{rubles} рублей = {converted:.2f} долларов.")
elif currency == 'евро':
        converted = rubles / euro
        print(f"{rubles} рублей = {converted:.2f} евро.")
else:
        print("Неверная валюта.")
