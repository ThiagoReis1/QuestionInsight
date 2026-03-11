lim = float(input())
a = float(input("valor a: "))
b = float(input("valor b: "))
c = float(input("valor c: "))
d = float(input("valor D: "))

total = a +b + c + d
if(total <= lim):
	print(round(total, 2))
	print("Dentro do limite")
else:
	print(round(total ,2))
	print("Estourou o limite")