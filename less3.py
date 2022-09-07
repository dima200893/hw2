# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# (1+1\n)^n


n = int(input('Введите количество чисел в последовательности: '))
list=[]
summ = 0
for i in range(0, n):
    value = (1+1/n)**n
    list.append(value)
    summ += value
print(list, end=',')
print('Сумма всех чисел последовательности:', summ)