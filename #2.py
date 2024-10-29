# 2 Задание
liters = float(input("Введите количество литров топлива: "))
price_per_liter = float(input("Введите стоимость за литр: "))
distance = float(input("Введите пройденное расстояние (в км): "))

total_cost = liters * price_per_liter
consumption_per_100km = (liters / distance) * 100
print(f"Потрачено денег на топливо: {total_cost:.2f} руб.")
print(f"Расход топлива на 100 км: {consumption_per_100km:.2f} л.")