# Test
Тестовое задание 

В этом тестовом задании я выполнил 4\6 тестовых чек-поинтов.
Я соеденил 2 чекпоинта в одну ф-цию поэтому в дальнейшем эти ЧП будут выглядеть как (1-2)

Для выполнения поставленных задач необходимо было работать с файлом, в котором находится очень много чисел. К выполению задачи я приступил на Python.

1-2 #min-max вывести минимальное и максимальное число в файле.

file = open('C:/Users/Даня/Desktop/10m.txt/10m.txt') 

данная строка отвечает за переменную, в которой хранится открытый файл.

lst = []


тут я инициализировал пустой список элементов, (решил пойти через списки, так как это единственное, что пришло на ум), в который я буду записывать каждый
элемент числа с файла в новый список 

    for i in file:
        lst.append(int(i))
       
выше инициализировал запись каждого числа с файла (i) в новый список

    minimum = min(lst)
    maximum = max(lst)


выше инициализировал непосредственно переменные, которые принимают минимальное и максимальное число.

3 #average среднее орифметическое

    for i in file:
        lst.append(int(i))
       
так же инициализировал запись каждого числа с файла (i) в новый список

summa = sum(lst) - инициализировал переменную, которая будет хранить в себе сумму всех элементов списка

print('Сумма всех чисел: ', summa)
print('Общее число всех чисел: ', + len(lst)) 
print('Среднее арифметическое  = ', summa//len(lst))
#len(lst) = кол-во элементов списка, так как len(lst) хранит в себе длинну всех чисел с файла

#mediana

    for i in file:
        lst.append(int(i))
        
так же инициализировал запись каждого числа с файла (i) в новый список

    print('Середина данного списка: ', middle)
    print('Следующий элемент от середины спика: ', nextIn)
    print('Предыдущий элемент от середины списка: ' ,prevIn)
    print('Медиана: ', median)
