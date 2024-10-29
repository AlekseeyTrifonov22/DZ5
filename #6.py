# 6 Задание
correct_answers = int(input("Введите количество правильных ответов: "))
total_questions = int(input("Введите общее количество вопросов: "))

percentage = (correct_answers / total_questions) * 100
if percentage < 50:
    grade = "Неудовлетворительно"
elif 50 <= percentage < 70:
    grade = "Удовлетворительно"
else:
    grade = "Удовлетворительно"

print(f"Процент правильных ответов: {percentage:.2f}% - Оценка: {grade}")