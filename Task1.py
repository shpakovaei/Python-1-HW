# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.

number = int (input('Введите номер дня недели: '))

if (number >= 1 and number <= 7):
    if (number == 6 or number == 7):

        print ('Этот день выходной')
    else: 
        print ('Этот день рабочий')

else:
    print ('Такого дня недели не существует')