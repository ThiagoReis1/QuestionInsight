p1= float(input("digite a nota 1: "))
p2= float(input("digite a nota 2: "))
p3= float(input("digite a nota 3: "))
m= (p1+p2+p3)/3
if (m >= 7):
	print(round(m,1))
	print("Aprovado")
else:
	print(round(m,1))
	print("Reprovado")