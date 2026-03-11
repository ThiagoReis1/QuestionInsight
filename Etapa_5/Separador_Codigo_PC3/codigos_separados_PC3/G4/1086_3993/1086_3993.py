n1 = float(input("Nota um: "))
n2 = float(input("Nota dois: "))
n3 = float(input("Nota tres: "))
m = (n1 + n2 + n3)/3
if(m >= 7):
	print(round(m,1))
	print("Aprovado")
else:
	print(round(m,1))
	print("Reprovado")