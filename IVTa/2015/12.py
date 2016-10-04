#Задача 12. Вариант 3.
#1-50. Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python
#гл. 6).
# Gilfanov A. I.
# 29.09.2016
i=0
x=0
pole = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]"]
print("Игра крестики нолики для того чтобы походить укажите номур ячейки для хода")
print(pole[0],pole[1],pole[2])
print(pole[3],pole[4],pole[5])
print(pole[6],pole[7],pole[8])
while True:
    if pole[0]==pole[1] and pole[1]==pole[2]:
        print("Выйграл: ",pole[1])
        break
    elif pole[3]==pole[4] and pole[4]==pole[5]:
        print("Выйграл: ",pole[4])
        break
    elif pole[6]==pole[7] and pole[7]==pole[8]:
        print("Выйграл: ",pole[7])
        break
    elif pole[0]==pole[3] and pole[3]==pole[6]:
        print("Выйграл: ",pole[3])
        break
    elif pole[1]==pole[4] and pole[4]==pole[7]:
        print("Выйграл: ",pole[1])
        break
    elif pole[2]==pole[5] and pole[5]==pole[8]:
        print("Выйграл: ",pole[1])
        break
    elif pole[2]==pole[4] and pole[4]==pole[6]:
        print("Выйграл: ",pole[1])
        break
    elif pole[0]==pole[4] and pole[4]==pole[8]:
        print("Выйграл: ",pole[1])
        break
    i+=1
    if i%2==0:
        while True:
            Z=int(input("Нолики: "))
            if pole[Z-1]=="[X]":
                print("Выберете другую клетку")
                continue
            elif pole[Z-1]=="[0]":
                print("Выберете другую клетку")
                continue
            else:
                pole[Z-1]="[0]"
                print(pole[0],pole[1],pole[2])
                print(pole[3],pole[4],pole[5])
                print(pole[6],pole[7],pole[8])
                break
    else:
        while True:
            Z=int(input("Крестики: "))
            if pole[Z-1]=="[X]":
                print("Выберете другую клетку")
                continue
            elif pole[Z-1]=="[0]":
                print("Выберете другую клетку")
                continue
            else:
                pole[Z-1]="[X]"
                print(pole[0],pole[1],pole[2])
                print(pole[3],pole[4],pole[5])
                print(pole[6],pole[7],pole[8])
                break
