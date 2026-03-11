lim = float(input())
a = float(input())
b = float(input())
c = float(input())
d = float(input())

total = (a+b+c+d)
total2 = (round(total, 2))

if(total2<=lim):
	print(total2)
	print("Dentro do limite")
else:
	print(total2)
	print("Estourou o limite")
	