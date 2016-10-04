#Задача 12. Вариант 3.
#1-50. Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python
#гл. 6).
# Gilfanov A. I.
# 29.09.2016
i=0
x=0
d=0
pole = ["[1]","[2]","[3]","[4]","[5]","[6]","[7]","[8]","[9]"]
print("Игра крестики нолики для того чтобы походить укажите номур ячейки для хода")
print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
print("Игра начинается!")
while True:
    if pole[0]==pole[1] and pole[1]==pole[2]:
        if i%2==1:
            print("Выйграл: X")
            input("Нажмите Enter для выхода")
        else:
            print("Выйграл: 0")
            input("Нажмите Enter для выхода")
        break
    elif pole[3]==pole[4] and pole[4]==pole[5]:
        if i%2==1:
            print("Выйграл: X")
            input("Нажмите Enter для выхода")
        else:
            print("Выйграл: 0")
            input("Нажмите Enter для выхода")
        break
    elif pole[6]==pole[7] and pole[7]==pole[8]:
        if i%2==1:
            print("Выйграл: X")
            input("Нажмите Enter для выхода")
        else:
            print("Выйграл: 0")
            input("Нажмите Enter для выхода")
        break
    elif pole[0]==pole[3] and pole[3]==pole[6]:
        if i%2==1:
            print("Выйграл: X")
            input("Нажмите Enter для выхода")
        else:
            print("Выйграл: 0")
            input("Нажмите Enter для выхода")
        break
    elif pole[1]==pole[4] and pole[4]==pole[7]:
        if i%2==1:
            print("Выйграл: X")
            input("Нажмите Enter для выхода")
        else:
            print("Выйграл: 0")
            input("Нажмите Enter для выхода")
        break
    elif pole[2]==pole[5] and pole[5]==pole[8]:
        if i%2==1:
            print("Выйграл: X")
            input("Нажмите Enter для выхода")
        else:
            print("Выйграл: 0")
            input("Нажмите Enter для выхода")
        break
    elif pole[2]==pole[4] and pole[4]==pole[6]:
        if i%2==1:
            print("Выйграл: X")
            input("Нажмите Enter для выхода")
        else:
            print("Выйграл: 0")
            input("Нажмите Enter для выхода")
        break
    elif pole[0]==pole[4] and pole[4]==pole[8]:
        if i%2==1:
            print("Выйграл: X")
            input("Нажмите Enter для выхода")
        else:
            print("Выйграл: 0")
            input("Нажмите Enter для выхода")
        break
    i+=1
    if i%2==1:
        d+=1
        if d==1:
            print("Ход бота 1")
            pole[4]="[X]"
            print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
        elif d==2:
            print("Ход бота 2")
            if pole[0]=="[0]":
                pole[2]="[X]"
                print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif pole[5]!="[0]" and pole[3]!="[0]":
                pole[3]="[X]"
                print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif pole[0]!="[0]":
                pole[0]="[X]"
                print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
        elif d==3:
            print("Ход бота 3")
            if (pole[0]=="[X]" and pole[1]=="[X]" and pole[2]!="[0]")\
                or (pole[0]=="[X]" and pole[2]=="[X]" and pole[1]!="[0]")\
                or (pole[1]=="[X]" and pole[2]=="[X]" and pole[0]!="[0]")\
                or (pole[3]=="[X]" and pole[4]=="[X]" and pole[5]!="[0]")\
                or (pole[3]=="[X]" and pole[5]=="[X]" and pole[4]!="[0]")\
                or (pole[4]=="[X]" and pole[5]=="[X]" and pole[3]!="[0]")\
                or (pole[6]=="[X]" and pole[7]=="[X]" and pole[8]!="[0]")\
                or (pole[6]=="[X]" and pole[8]=="[X]" and pole[7]!="[0]")\
                or (pole[7]=="[X]" and pole[8]=="[X]" and pole[6]!="[0]")\
                or (pole[0]=="[X]" and pole[3]=="[X]" and pole[6]!="[0]")\
                or (pole[0]=="[X]" and pole[6]=="[X]" and pole[3]!="[0]")\
                or (pole[3]=="[X]" and pole[6]=="[X]" and pole[0]!="[0]")\
                or (pole[1]=="[X]" and pole[4]=="[X]" and pole[7]!="[0]")\
                or (pole[1]=="[X]" and pole[7]=="[X]" and pole[4]!="[0]")\
                or (pole[4]=="[X]" and pole[7]=="[X]" and pole[1]!="[0]")\
                or (pole[2]=="[X]" and pole[5]=="[X]" and pole[8]!="[0]")\
                or (pole[2]=="[X]" and pole[8]=="[X]" and pole[5]!="[0]")\
                or (pole[5]=="[X]" and pole[8]=="[X]" and pole[2]!="[0]")\
                or (pole[0]=="[X]" and pole[4]=="[X]" and pole[8]!="[0]")\
                or (pole[0]=="[X]" and pole[8]=="[X]" and pole[4]!="[0]")\
                or (pole[4]=="[X]" and pole[8]=="[X]" and pole[0]!="[0]")\
                or (pole[2]=="[X]" and pole[4]=="[X]" and pole[6]!="[0]")\
                or (pole[2]=="[X]" and pole[6]=="[X]" and pole[4]!="[0]")\
                or (pole[4]=="[X]" and pole[6]=="[X]" and pole[2]!="[0]"):
                    if pole[0]=="[X]" and pole[1]=="[X]" and pole[2]!="[0]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[2]=="[X]" and pole[1]!="[0]":
                        pole[1]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[X]" and pole[2]=="[X]" and pole[0]!="[0]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[X]" and pole[4]=="[X]" and pole[5]!="[0]":
                        pole[5]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[X]" and pole[5]=="[X]" and pole[4]!="[0]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[X]" and pole[5]=="[X]" and pole[3]!="[0]":
                        pole[3]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[6]=="[X]" and pole[7]=="[X]" and pole[8]!="[0]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[6]=="[X]" and pole[8]=="[X]" and pole[7]!="[0]":
                        pole[7]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[7]=="[X]" and pole[8]=="[X]" and pole[6]!="[0]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[3]=="[X]" and pole[6]!="[0]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[6]=="[X]" and pole[3]!="[0]":
                        pole[3]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[X]" and pole[6]=="[X]" and pole[0]!="[0]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[X]" and pole[4]=="[X]" and pole[7]!="[0]":
                        pole[7]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[X]" and pole[7]=="[X]" and pole[4]!="[0]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[X]" and pole[7]=="[X]" and pole[1]!="[0]":
                        pole[1]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[X]" and pole[5]=="[X]" and pole[8]!="[0]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[X]" and pole[8]=="[X]" and pole[5]!="[0]":
                        pole[5]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[5]=="[X]" and pole[8]=="[X]" and pole[2]!="[0]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[4]=="[X]" and pole[8]!="[0]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[8]=="[X]" and pole[4]!="[0]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[X]" and pole[8]=="[X]" and pole[0]!="[0]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[X]" and pole[4]=="[X]" and pole[6]!="[0]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[X]" and pole[6]=="[X]" and pole[4]!="[0]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[X]" and pole[6]=="[X]" and pole[2]!="[0]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif (pole[0]=="[0]" and pole[1]=="[0]" and pole[2]!="[X]")\
                or (pole[0]=="[0]" and pole[2]=="[0]" and pole[1]!="[X]")\
                or (pole[1]=="[0]" and pole[2]=="[0]" and pole[0]!="[X]")\
                or (pole[3]=="[0]" and pole[4]=="[0]" and pole[5]!="[X]")\
                or (pole[3]=="[0]" and pole[5]=="[0]" and pole[4]!="[X]")\
                or (pole[4]=="[0]" and pole[5]=="[0]" and pole[3]!="[X]")\
                or (pole[6]=="[0]" and pole[7]=="[0]" and pole[8]!="[X]")\
                or (pole[6]=="[0]" and pole[8]=="[0]" and pole[7]!="[X]")\
                or (pole[7]=="[0]" and pole[8]=="[0]" and pole[6]!="[X]")\
                or (pole[0]=="[0]" and pole[3]=="[0]" and pole[6]!="[X]")\
                or (pole[0]=="[0]" and pole[6]=="[0]" and pole[3]!="[X]")\
                or (pole[3]=="[0]" and pole[6]=="[0]" and pole[0]!="[X]")\
                or (pole[1]=="[0]" and pole[4]=="[0]" and pole[7]!="[X]")\
                or (pole[1]=="[0]" and pole[7]=="[0]" and pole[4]!="[X]")\
                or (pole[4]=="[0]" and pole[7]=="[0]" and pole[1]!="[X]")\
                or (pole[2]=="[0]" and pole[5]=="[0]" and pole[8]!="[X]")\
                or (pole[2]=="[0]" and pole[8]=="[0]" and pole[5]!="[X]")\
                or (pole[5]=="[0]" and pole[8]=="[0]" and pole[2]!="[X]")\
                or (pole[0]=="[0]" and pole[4]=="[0]" and pole[8]!="[X]")\
                or (pole[0]=="[0]" and pole[8]=="[0]" and pole[4]!="[X]")\
                or (pole[4]=="[0]" and pole[8]=="[0]" and pole[0]!="[X]")\
                or (pole[2]=="[0]" and pole[4]=="[0]" and pole[6]!="[X]")\
                or (pole[2]=="[0]" and pole[6]=="[0]" and pole[4]!="[X]")\
                or (pole[4]=="[0]" and pole[6]=="[0]" and pole[2]!="[X]"):
                    if pole[0]=="[0]" and pole[1]=="[0]" and pole[2]!="[X]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[0]" and pole[2]=="[0]" and pole[1]!="[X]":
                        pole[1]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[0]" and pole[2]=="[0]" and pole[0]!="[X]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[0]" and pole[4]=="[0]" and pole[5]!="[X]":
                        pole[5]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[0]" and pole[5]=="[0]" and pole[4]!="[X]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[0]" and pole[5]=="[0]" and pole[3]!="[X]":
                        pole[3]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[6]=="[0]" and pole[7]=="[0]" and pole[8]!="[X]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[6]=="[0]" and pole[8]=="[0]" and pole[7]!="[X]":
                        pole[7]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[7]=="[0]" and pole[8]=="[0]" and pole[6]!="[X]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[0]" and pole[3]=="[0]" and pole[6]!="[X]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[0]" and pole[6]=="[0]" and pole[3]!="[X]":
                        pole[3]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[0]" and pole[6]=="[0]" and pole[0]!="[X]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[0]" and pole[4]=="[0]" and pole[7]!="[X]":
                        pole[7]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[0]" and pole[7]=="[0]" and pole[4]!="[X]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[0]" and pole[7]=="[0]" and pole[1]!="[X]":
                        pole[1]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[0]" and pole[5]=="[0]" and pole[8]!="[X]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[0]" and pole[8]=="[0]" and pole[5]!="[X]":
                        pole[5]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[5]=="[0]" and pole[8]=="[0]" and pole[2]!="[X]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[0]" and pole[4]=="[0]" and pole[8]!="[X]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[0]" and pole[8]=="[0]" and pole[4]!="[X]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[0]" and pole[8]=="[0]" and pole[0]!="[X]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[0]" and pole[4]=="[0]" and pole[6]!="[X]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[0]" and pole[6]=="[0]" and pole[4]!="[X]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[0]" and pole[6]=="[0]" and pole[2]!="[X]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif pole[5]=="[0]" and (pole[8]=="[0]" or pole[2]=="[0]"):
                if pole[2]=="[0]":
                    pole[8]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[8]=="[0]":
                    pole[2]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif (pole[0]=="[0]" and pole[2]=="[0]") or (pole[0]=="[0]" and pole[1]=="[0]") or (pole[1]=="[0]" and pole[2]=="[0]"):
                if pole[0]=="[0]" and pole[2]=="[0]":
                    pole[1]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[0]=="[0]" and pole[1]=="[0]":
                    pole[2]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[1]=="[0]" and pole[2]=="[0]":
                    pole[0]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif pole[0]=="[X]" and pole[3]!="[0]":
                pole[5]="[X]"
                print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif pole[0]=="[X]" and pole[3]=="[0]":
                pole[6]="[X]"
                print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif pole[3]=="[X]" and pole[0]!="[0]":
                pole[0]="[X]"
                print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")                
            elif pole[3]=="[X]" and pole[0]=="[0]":
                pole[6]="[X]"
                print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
        elif d==4:
            print("Ход бота 4")
            if (pole[0]=="[X]" and pole[1]=="[X]" and pole[2]!="[0]")\
                or (pole[0]=="[X]" and pole[2]=="[X]" and pole[1]!="[0]")\
                or (pole[1]=="[X]" and pole[2]=="[X]" and pole[0]!="[0]")\
                or (pole[3]=="[X]" and pole[4]=="[X]" and pole[5]!="[0]")\
                or (pole[3]=="[X]" and pole[5]=="[X]" and pole[4]!="[0]")\
                or (pole[4]=="[X]" and pole[5]=="[X]" and pole[3]!="[0]")\
                or (pole[6]=="[X]" and pole[7]=="[X]" and pole[8]!="[0]")\
                or (pole[6]=="[X]" and pole[8]=="[X]" and pole[7]!="[0]")\
                or (pole[7]=="[X]" and pole[8]=="[X]" and pole[6]!="[0]")\
                or (pole[0]=="[X]" and pole[3]=="[X]" and pole[6]!="[0]")\
                or (pole[0]=="[X]" and pole[6]=="[X]" and pole[3]!="[0]")\
                or (pole[3]=="[X]" and pole[6]=="[X]" and pole[0]!="[0]")\
                or (pole[1]=="[X]" and pole[4]=="[X]" and pole[7]!="[0]")\
                or (pole[1]=="[X]" and pole[7]=="[X]" and pole[4]!="[0]")\
                or (pole[4]=="[X]" and pole[7]=="[X]" and pole[1]!="[0]")\
                or (pole[2]=="[X]" and pole[5]=="[X]" and pole[8]!="[0]")\
                or (pole[2]=="[X]" and pole[8]=="[X]" and pole[5]!="[0]")\
                or (pole[5]=="[X]" and pole[8]=="[X]" and pole[2]!="[0]")\
                or (pole[0]=="[X]" and pole[4]=="[X]" and pole[8]!="[0]")\
                or (pole[0]=="[X]" and pole[8]=="[X]" and pole[4]!="[0]")\
                or (pole[4]=="[X]" and pole[8]=="[X]" and pole[0]!="[0]")\
                or (pole[2]=="[X]" and pole[4]=="[X]" and pole[6]!="[0]")\
                or (pole[2]=="[X]" and pole[6]=="[X]" and pole[4]!="[0]")\
                or (pole[4]=="[X]" and pole[6]=="[X]" and pole[2]!="[0]"):
                    if pole[0]=="[X]" and pole[1]=="[X]" and pole[2]!="[0]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[2]=="[X]" and pole[1]!="[0]":
                        pole[1]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[X]" and pole[2]=="[X]" and pole[0]!="[0]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[X]" and pole[4]=="[X]" and pole[5]!="[0]":
                        pole[5]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[X]" and pole[5]=="[X]" and pole[4]!="[0]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[X]" and pole[5]=="[X]" and pole[3]!="[0]":
                        pole[3]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[6]=="[X]" and pole[7]=="[X]" and pole[8]!="[0]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[6]=="[X]" and pole[8]=="[X]" and pole[7]!="[0]":
                        pole[7]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[7]=="[X]" and pole[8]=="[X]" and pole[6]!="[0]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[3]=="[X]" and pole[6]!="[0]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[6]=="[X]" and pole[3]!="[0]":
                        pole[3]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[3]=="[X]" and pole[6]=="[X]" and pole[0]!="[0]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[X]" and pole[4]=="[X]" and pole[7]!="[0]":
                        pole[7]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[1]=="[X]" and pole[7]=="[X]" and pole[4]!="[0]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[X]" and pole[7]=="[X]" and pole[1]!="[0]":
                        pole[1]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[X]" and pole[5]=="[X]" and pole[8]!="[0]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[X]" and pole[8]=="[X]" and pole[5]!="[0]":
                        pole[5]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[5]=="[X]" and pole[8]=="[X]" and pole[2]!="[0]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[4]=="[X]" and pole[8]!="[0]":
                        pole[8]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[0]=="[X]" and pole[8]=="[X]" and pole[4]!="[0]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[X]" and pole[8]=="[X]" and pole[0]!="[0]":
                        pole[0]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[X]" and pole[4]=="[X]" and pole[6]!="[0]":
                        pole[6]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[2]=="[X]" and pole[6]=="[X]" and pole[4]!="[0]":
                        pole[4]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    elif pole[4]=="[X]" and pole[6]=="[X]" and pole[2]!="[0]":
                        pole[2]="[X]"
                        print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif (pole[0]=="[0]" and pole[1]=="[0]" and pole[2]!="[X]")\
                or (pole[0]=="[0]" and pole[2]=="[0]" and pole[1]!="[X]")\
                or (pole[1]=="[0]" and pole[2]=="[0]" and pole[0]!="[X]")\
                or (pole[3]=="[0]" and pole[4]=="[0]" and pole[5]!="[X]")\
                or (pole[3]=="[0]" and pole[5]=="[0]" and pole[4]!="[X]")\
                or (pole[4]=="[0]" and pole[5]=="[0]" and pole[3]!="[X]")\
                or (pole[6]=="[0]" and pole[7]=="[0]" and pole[8]!="[X]")\
                or (pole[6]=="[0]" and pole[8]=="[0]" and pole[7]!="[X]")\
                or (pole[7]=="[0]" and pole[8]=="[0]" and pole[6]!="[X]")\
                or (pole[0]=="[0]" and pole[3]=="[0]" and pole[6]!="[X]")\
                or (pole[0]=="[0]" and pole[6]=="[0]" and pole[3]!="[X]")\
                or (pole[3]=="[0]" and pole[6]=="[0]" and pole[0]!="[X]")\
                or (pole[1]=="[0]" and pole[4]=="[0]" and pole[7]!="[X]")\
                or (pole[1]=="[0]" and pole[7]=="[0]" and pole[4]!="[X]")\
                or (pole[4]=="[0]" and pole[7]=="[0]" and pole[1]!="[X]")\
                or (pole[2]=="[0]" and pole[5]=="[0]" and pole[8]!="[X]")\
                or (pole[2]=="[0]" and pole[8]=="[0]" and pole[5]!="[X]")\
                or (pole[5]=="[0]" and pole[8]=="[0]" and pole[2]!="[X]")\
                or (pole[0]=="[0]" and pole[4]=="[0]" and pole[8]!="[X]")\
                or (pole[0]=="[0]" and pole[8]=="[0]" and pole[4]!="[X]")\
                or (pole[4]=="[0]" and pole[8]=="[0]" and pole[0]!="[X]")\
                or (pole[2]=="[0]" and pole[4]=="[0]" and pole[6]!="[X]")\
                or (pole[2]=="[0]" and pole[6]=="[0]" and pole[4]!="[X]")\
                or (pole[4]=="[0]" and pole[6]=="[0]" and pole[2]!="[X]"):
                if pole[0]=="[0]" and pole[1]=="[0]" and pole[2]!="[X]":
                    pole[2]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[0]=="[0]" and pole[2]=="[0]" and pole[1]!="[X]":
                    pole[1]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[1]=="[0]" and pole[2]=="[0]" and pole[0]!="[X]":
                    pole[0]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[3]=="[0]" and pole[4]=="[0]" and pole[5]!="[X]":
                    pole[5]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[3]=="[0]" and pole[5]=="[0]" and pole[4]!="[X]":
                    pole[4]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[4]=="[0]" and pole[5]=="[0]" and pole[3]!="[X]":
                    pole[3]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[6]=="[0]" and pole[7]=="[0]" and pole[8]!="[X]":
                    pole[8]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[6]=="[0]" and pole[8]=="[0]" and pole[7]!="[X]":
                    pole[7]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[7]=="[0]" and pole[8]=="[0]" and pole[6]!="[X]":
                    pole[6]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[0]=="[0]" and pole[3]=="[0]" and pole[6]!="[X]":
                    pole[6]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[0]=="[0]" and pole[6]=="[0]" and pole[3]!="[X]":
                    pole[3]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[3]=="[0]" and pole[6]=="[0]" and pole[0]!="[X]":
                    pole[0]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[1]=="[0]" and pole[4]=="[0]" and pole[7]!="[X]":
                    pole[7]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[1]=="[0]" and pole[7]=="[0]" and pole[4]!="[X]":
                    pole[4]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[4]=="[0]" and pole[7]=="[0]" and pole[1]!="[X]":
                    pole[1]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[2]=="[0]" and pole[5]=="[0]" and pole[8]!="[X]":
                    pole[8]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[2]=="[0]" and pole[8]=="[0]" and pole[5]!="[X]":
                    pole[5]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[5]=="[0]" and pole[8]=="[0]" and pole[2]!="[X]":
                    pole[2]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[0]=="[0]" and pole[4]=="[0]" and pole[8]!="[X]":
                    pole[8]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[0]=="[0]" and pole[8]=="[0]" and pole[4]!="[X]":
                    pole[4]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[4]=="[0]" and pole[8]=="[0]" and pole[0]!="[X]":
                    pole[0]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[2]=="[0]" and pole[4]=="[0]" and pole[6]!="[X]":
                    pole[6]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[2]=="[0]" and pole[6]=="[0]" and pole[4]!="[X]":
                    pole[4]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[4]=="[0]" and pole[6]=="[0]" and pole[2]!="[X]":
                    pole[2]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif (pole[0]=="[0]" and pole[2]=="[0]") or (pole[0]=="[0]" and pole[1]=="[0]") or (pole[1]=="[0]" and pole[2]=="[0]"):
                if pole[0]=="[0]" and pole[2]=="[0]":
                    pole[1]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[0]=="[0]" and pole[1]=="[0]":
                    pole[2]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[1]=="[0]" and pole[2]=="[0]":
                    pole[0]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif pole[3]=="[X]" and pole[0]=="[0]":
                if pole[6]!="[0]":
                    pole[6]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[5]!="[0]":
                    pole[5]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[8]!="[0]":
                    pole[8]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
            elif pole[3]=="[X]" and pole[6]=="[0]":
                if pole[1]!="[0]":
                    pole[1]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[2]!="[0]":
                    pole[2]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                elif pole[5]!="[0]":
                    pole[5]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
        elif d==5:
            print("Ход бота 5")
            for j in range(9):
                if pole[j-1]!="[X]" and pole[j-1]!="[0]":
                    pole[j-1]="[X]"
                    print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                    print("Ничья")
                    input("Нажмите Enter для выхода")
            break
    else:
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
                print("\n",pole[0],pole[1],pole[2],"\n",pole[3],pole[4],pole[5],"\n",pole[6],pole[7],pole[8],"\n")
                break
