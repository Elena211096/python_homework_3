#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
#максимальным и минимальным значением дробной части элементов.


array = [1.2, 1.3, 1.14, 1.51, 1.02, 5]
min_digit = 1
max_digit = 0
for i in range(len(array)):
    current_digit = array[i] % 1
    if current_digit != 0:
        if current_digit > max_digit:
            max_digit = current_digit
        elif current_digit < min_digit:
            min_digit = current_digit
result = max_digit - min_digit, 2
print(result)
