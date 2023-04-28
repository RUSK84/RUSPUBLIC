a = float(input('Введите первое число: '))
if a==0:
    print ('Введите значение не равное 0')
    a = float(input('Введите первое число: '))


znac = input('Введите действие: ')
znac_cor = ['+', '-', '*', '/']
for i in znac_cor:
    if znac not in znac_cor:
        print('Введите правильную арифметическую операцию!!!')
        znac = input('Введите действие: ')


b = float(input('Введите второе число: '))
if b==0:
    print ('Введите значение не равное 0')
    b = float(input('Введите второе число: '))

if znac == znac_cor[0]:
    znacenie = a+b
    print ('Результат: ', znacenie)
elif znac == znac_cor[1]:
    znacenie = a - b
    print('Результат: ', znacenie)
elif znac == znac_cor[2]:
    znacenie = a * b
    print('Результат: ', znacenie)
elif znac == znac_cor[3]:
    znacenie = a / b
    print('Результат: ', znacenie)
elif znac == znac_cor[4]:
    znacenie = a ** b
    print('Результат: ', znacenie)
