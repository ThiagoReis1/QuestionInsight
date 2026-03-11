n1 = float(input("Digite a nota 1:"))
n2 = float(input("Digite a nota 2:"))
n3 = float(input("Digite a nota 3:"))
n4 = float(input("Digite a nota 4:"))

ma = (n1 + n2 + n3 + n4) / 4
ma = round(ma, 2)
print(ma)

if(ma >= 7):
	print("Aprovado")
	
else:
	print("Reprovado")