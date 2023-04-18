# bmi_calculator.py

# Ввод данных от пользователя
weight = float(input("Введите ваш вес в килограммах: "))
height = float(input("Введите ваш рост в метрах: "))

# Расчет индекса массы тела (ИМТ)
bmi = weight / (height ** 2)

# Вывод результата
print("Ваш ИМТ: {:.2f}".format(bmi))
