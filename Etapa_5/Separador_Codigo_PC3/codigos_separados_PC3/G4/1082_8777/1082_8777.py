a=float(input("Nota Obtida: "))
b=float(input("Nota Obtida: "))
c=float(input("Nota Obtida:"))
d=float(input("Nota Obtida: "))
e=float(input("Nota Obtida: "))
me= round((a+b+c+d+e)/5, 1)
if me >= 5.0:
	print(me)
	print("Aprovado")
else:
	print(me)
	print("Reprovado")