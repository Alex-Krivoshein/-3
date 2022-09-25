#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.


my_list = [2, 3, 5, 9, 3]
print(sum(my_list[1::2]))


#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.


my_list = [2, 3, 4, 5, 6]
result_list = []
for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i]*my_list[len(my_list)-1-i])
print(result_list)


#Напишите программу, которая будет преобразовывать десятичное число в двоичное.


a = ""
b = int(input("Введите число: \b"))
while b != 0:
    a = str(b%2) + a
    b //=2
print(a)


#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.


k = int(input('Введите число: '))

def get_fibonacci(k):
    fibo_nums = []
    a, b = 1, 1
    for i in range(k-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(k)
print(get_fibonacci(k))
print(fibo_nums.index(0))