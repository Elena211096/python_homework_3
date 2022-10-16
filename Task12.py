#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.


array = [1, 2, 3, 4, 5, 6, 7, 8]
new_array = []
for i in range(len(array) // 2):
    new_array.append(array[i] * array[len(array) - 1 -i])
print(new_array)
