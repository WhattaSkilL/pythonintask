#Задача 12. Вариант 3.
#1-50. Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python
#гл. 6).
# Gilfanov A. I.
# 29.09.2016
XY11="-"
XY12="-"
XY13="-"
XY21="-"
XY22="-"
XY23="-"
XY31="-"
XY32="-"
XY33="-"
while(((XY11 and XY12 and XY13)=="0" or "X") or ((XY11 and XY22 and XY33)=="0" or "X") or ((XY11 and XY21 and XY31)=="0" or "X") or ((XY12 and XY22 and XY32)=="0" or "X") or ((XY31 and XY32 and XY33)=="0" or "X") or ((XY21 and XY22 and XY23)=="0" or "X") or ((XY13 and XY23 and XY33)=="0" or "X") or ((XY31 and XY22 and XY13)=="0" or "X"))
print('\n',XY11, XY21, XY31,'\n',XY12, XY22, XY32,'\n',XY13, XY23, XY33)
X=input("Введите координату по X")
Y=input("Введите координату по Y")
