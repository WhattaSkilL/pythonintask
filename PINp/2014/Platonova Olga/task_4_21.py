# Задача 4. Вариант 21.
#Напишите программу, которая выводит имя, под которым скрывается Филип Ауреол Теофраст Бомбаст фон Гогенгейм. Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Platonova O. A.
# 29.05.2016

name="Филип Ауреол Теофраст Бомбаст фон Гогенгейм"
psevdo="Парацельс"
place="Айнзидельн (кантон Швиц, Швейцария)"
by=1493
bd=1541
interest="врач и алхимик"
print("Филип Ауреол Теофраст Бомбаст фон Гогенгейм более известен, как",interest,psevdo)
print("Место рождения:",place)
print("Год рождения:",by)
print("Влзраст:",bd-by)
print("область интерсеов:",interest)
input("\nНажмите Enter для выхода.")