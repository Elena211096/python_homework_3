#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


fibonachchi = [0, 1]
for i in range (8):
    fibonachchi.append(fibonachchi[-1] + fibonachchi[-2])
print(fibonachchi)


negative = [0, 1]
for n in range(8):
    negative.append(negative[-2] - negative[-1])
negative.reverse()


print(negative + fibonachchi[1:])
