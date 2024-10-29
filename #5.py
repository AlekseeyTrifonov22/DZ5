# 5 Задание
weight = float(input("Введите ваш вес (в кг): "))
height = float(input("Введите ваш рост (в м): "))

bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Недостаточный вес"
elif 18.5 <= bmi < 24.9:
    category = "Норма"
elif 25 <= bmi < 29.9:
    category = "Избыточный вес"
else:
    category = "Ожирение"

print(f"Ваш индекс массы тела (ВМІ): {bmi:.2f} - {category}")