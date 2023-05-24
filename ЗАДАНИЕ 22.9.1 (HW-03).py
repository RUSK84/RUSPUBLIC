import random
 #Получаем список чисел
while True: #Цыкл на проверку что числа целие в списке
  try:
     array = list(map(int, input('Введите целые числа (через пробел): ').split())) #Вводим последовательность чисел

  except ValueError: #Делаем проверку на правильность ввода данных, если данные не соответствуют условиям повторяем ввод
     print("!!!Ошибка ввода!!!")
     array = list(map(int, input('Введите целые числа (через пробел): ').split()))
  break

#Цыкл на проверку что вводимое число целие
while True:
  try:
     element = int(input('Введите целое числа : '))

  except ValueError:
     print("!!!Ошибка ввода!!!")
     element = int(input('Введите целое числа : '))
  break

#Добавляем введенное число в список и сортируем по возрастанию
array.append(element)
#Делаем быструю сортировку
def QuickSort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array) #элемент q выбирается случайным образом из списка при помощи функции choice из модуля random
        L = [] #собираются элементы, меньшие q
        M = [] #равные q
        R = [] #большие q
        for elem in array:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:            
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)


array=QuickSort(array)
print (array)
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
            #  рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, len(array)-1)) #Выводим номер введенного элемента

position=binary_search(array, element, 0, len(array)-1) #Присваиваем полученное значение позиции новому аргументу
#Выводим номера позиций элементов перед и после введенного значения
if position == len(array)-1:
    print(binary_search(array, element, 0, len(array)-1)-1, binary_search(array, element, 0, len(array)-1))
elif position ==0:
    print(binary_search(array, element, 0, len(array)-1), binary_search(array, element, 0, len(array)-1)+1)
else:
    print (binary_search(array, element, 0, len(array)-1)-1, binary_search(array, element, 0, len(array)-1)+1)
