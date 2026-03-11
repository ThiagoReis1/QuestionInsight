n1= float(input("digite o valor"))
n2= float(input("digite o valor"))
n3= float(input("digite o valor"))

td = (n1 + n2+ n3)/3
if (td >= 5.0):
	recado = ("Aprovado")
else:
	recado = ("Reprovado")
print(round(td,1))
print(recado)