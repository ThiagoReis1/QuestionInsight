from math import*

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
n4 = float(input("Nota 4: "))

m = (n1+n2+n3+n4)/4 

if m >= 7:
	print(round(m, 2))
	print("Aprovado")
else: 
	print(round(m, 2))
	print("Reprovado")