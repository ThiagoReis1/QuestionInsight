a = float(input("Nota 1: "))
b = float(input("Nota 2: "))
c = float(input("nota 3: "))
d = float(input("nota 4: "))

t = a + b + c + d
tt = t / 4

if tt >= 6:
	print(round(tt,1))
	print("Aprovado")
else:
	print(round(tt,1))
	print("Reprovado")