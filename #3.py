# 3 Задание
dohod = float(input("Введите ваш доход: "))

if dohod < 10000:
        nalog = dohod * 0.05
elif 10000 <= dohod <= 50000:
       nalog = dohod * 0.10
else:
        nalog = dohod * 0.15
print(f"Сумма налога: {nalog:.2f} руб.")