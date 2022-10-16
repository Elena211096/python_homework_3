#Напишите программу, которая будет преобразовывать десятичное число в двоичное.


print("Введите число: ")
input_number = int(input())
number_two = []
while input_number > 0:
    number_two.append(input_number % 2)
    input_number = input_number // 2
print(number_two)
