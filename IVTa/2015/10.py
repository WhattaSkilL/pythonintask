#Задача 10. Вариант 3.
#1-50. Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
#пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения.
# Gilfanov A. I.
# 29.09.2016
name=input("Введите имя персонажа: ")
print('Распределите характеристики персонажа. Для этого введите одну из характеристк и количество очков которые хотите потратить.Характеристики: Сила, Ловкость, Мудрость, Здоровье.')
P=30
S=0
M=0
A=0
H=0
E=0
while True:
    if E==0:
        print("---------------","\nИмя персонажа: ",name,"\nТекущие значения:","\nСила",S,"\nЛовкость",A,"\nМудрость",M,"\nЗдоровье",H,"\nОставшееся количество очков: ",P)
        print('Скажи мне ты желаешь "Повысить" или "Вернуть"?: ')
        print(name,": ")
        USE=input()
        if USE=="Повысить":
            print("Неизвестный: В чём именно ты желаешь стать лучше? ")
            print(name,":")
            CN=input()
            if CN == "Сила" or CN == "Ловкость" or CN == "Мудрость" or CN == "Здоровье":
                print("Неизвестный: Какое количество очков ты желаешь вложить?")
                print(name,": ")
                MP=int(input())
                if MP>P:
                    print("Неизвестный: Это не возможно")
                else:
                    if CN=="Сила": 
                        S+=MP
                        P-=MP
                        if P==0:
                            E+=1
                    elif CN=="Ловкость":
                        A+=MP
                        P-=MP
                        if P==0:
                            E+=1
                    elif CN=="Мудрость":
                        M+=MP
                        P-=MP
                        if P==0:
                            E+=1
                    elif CN=="Здоровье":
                        H+=MP
                        P-=MP
                        if P==0:
                            E+=1
            else:
                print("Неизвестный: Такой характеристики нету")
        elif USE=="Вернуть":
            print("Неизвестный: Назови что тебе в себе не нравится?")
            print(name,":")
            CN=input()
            if CN == "Сила" or CN == "Ловкость" or CN == "Мудрость" or CN == "Здоровье":
                print("Неизвестный: Какое количество очков ты желаешь вернуть?")
                print(name,": ",)
                MP=int(input())
                if CN=="Сила": 
                    if MP>S:
                        print("Неизвестный: Это не возможно")
                    else:
                        S-=MP
                        P+=MP
                elif CN=="Ловкость":
                    if MP>A:
                        print("Неизвестный: Это не возможно")
                    else:
                        A-=MP
                        P+=MP
                elif CN=="Мудрость":
                    if MP>M:
                        print("Неизвестный: Это не возможно")
                    else:
                        M-=MP
                        P+=MP
                elif CN=="Здоровье":
                    if MP>H:
                        print("Неизвестный: Это не возможно")
                    else:
                        H-=MP
                        P+=MP
            else:
                print("Неизвестный: Такой характеристики нету")
        else:
            print("Неизвестный: Я тебя не понял")
    else:
        print("---------------","\nИмя персонажа: ",name,"\nТекущие значения:","\nСила",S,"\nЛовкость",A,"\nМудрость",M,"\nЗдоровье",H)
        print("Неизвестный: Все очки распределены ты уверены что хочешь отправиться в путешевствие с такими характеристиками? (Да/Нет) \n")
        c=input(name,": ")
        if c=="Да":
            E+=1
            break
        elif c=="Нет":
            E=0
            continue
        else:
            print("Неизвестный: Очевидно вы не поняли моего вопроса")
            continue
print("Неизвестный:",name,"ты сделал свой выбор. Впереди тебя ждёт путь полон опастностей, но ты должен помнить что преград не существует и всегда есть способ обойти препятстве.","Удачи тебе",name,"!")
