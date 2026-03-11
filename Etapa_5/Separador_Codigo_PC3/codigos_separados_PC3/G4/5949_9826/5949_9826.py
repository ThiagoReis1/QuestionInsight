B = 3
C = 6
cpp = 5.50

a = input("digite B para bolo ou C para croissant: ")
b = int(input("quantidade de bc: "))
c = int(input("quantidade de cappuccinos: "))

if	a == "B":
	total = b * B
else:
	total = b * C
total1 = total + c * cpp
print(total1)