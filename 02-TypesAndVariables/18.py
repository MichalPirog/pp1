a=input("Podaj 1 bok: ")
b=input("Podaj 2 bok: ")
c=input("Podaj 3 bok: ")

a=int(a)
b=int(b)
c=int(c)

s=(a+b+b)/2

A=(s*(s-a)*(s-b)*(s-c))**(1/2)

print(A)