file = open('C:/Users/Даня/Desktop/10m.txt/10m.txt')
lst = []

#min-max 
def min_max(lst):

    for i in file:
        lst.append(int(i))
    minimum = min(lst)
    maximum = max(lst)

    print('Минимальное значение: ', minimum)
    print('Максимальное значение: ', maximum)
    
    
#average
def average(lst):

    for i in file:
        lst.append(int(i))

    summa = sum(lst) #для удобства
    print('Сумма всех чисел: ', summa)
    print('Общее число всех чисел: ', + len(lst)) 
    print('Среднее арифметическое  = ', summa//len(lst))
    #len(lst) = кол-во элементов списка

#mediana
def mediana(lst):

    for i in file:
        lst.append(int(i))

    middle = lst[len(lst)//2] #элемент середины списка
    nextIn = lst[len(lst)//2 + 1] #следующий элемент от середины списка
    prevIn = lst[len(lst)//2 - 1] #предыдущий элемент от середины списка
    median = (nextIn + prevIn)/2 #медиана
    #len(lst) = кол-во элементов списка

    print('Середина данного списка: ', middle)
    print('Следующий элемент от середины спика: ', nextIn)
    print('Предыдущий элемент от середины списка: ' ,prevIn)
    print('Медиана: ', median)

print(average(lst))
print(min_max(lst))
print(mediana(lst))
file.close()