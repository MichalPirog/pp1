# A user enters two integer numbers from the keyboard. Write a program that checks if at least one of them is positive.

x = int(input("Podaj 1 liczbe: "))
y =  int(input("Podaj 2 liczbe: "))

if x>0 or y>0:
    print("Prznamniej jedna z nich jest dodatnia")
else:
    print("Żadna z nich nie jest dodatnia")
