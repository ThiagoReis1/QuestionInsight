n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))

ma = (n1 + n2 + n3)/3
aprovado = ("Aprovado")
reprovado = ("Reprovado")

print(round(ma, 1))
if(ma >= 7):

	print(aprovado)
	 
else:
     
	print(reprovado)