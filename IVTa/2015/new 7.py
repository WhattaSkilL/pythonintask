#Задача 7. Вариант 3.
#Разработайте систему начисления очков для задачи 6, в соответствии с которой
#игрок получал бы большее количество баллов за меньшее количество попыток.
# Gilfanov A. I.
# 29.09.2016
import random
Z=10000
Y="Птица"
X=(random.choice(["Ред", "Чак", "Бомб", "Матильда", "Хэл", "Теренс", "Бабблз",]))
while X != Y:
    Y=input("Введите имя птички которую я загадал :)")
    if X != Y:
        Z-=1000;print("Увы но нет :с -1000 очков. У вас осталос:",Z) 
else:
    print("Поздравляю вы угадали! Ваше количество очков: ",Z)