# Задача 5. Вариант 47
# Напишите программу, которая бы при запуске случайным образом отображала название одного из четырех океанов Земли.

# Dubs A. E.
# 14.04.2016

import random 

print ("Программа случайным образом отображала название одного из четырех океанов Земли")

oceans = ('Тихий океан','Северный Ледовитый океан','Индийский океан','Атлантический океан')

print(random.choice(oceans))

input ("\n\n Нажмите Enter для выхода.")