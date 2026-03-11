n1 = float(input("nota da prova 1: "))
n2 = float(input("nota da prova 2: "))
n3 = float(input("nota da prova 3: "))
n4 = float(input("nota da prova 4: "))

ma = (n1 + n2 + n3 + n4)/4

print(round(ma, 1))

if(ma >=6):
	print("Aprovado")
else:
	print("Reprovado")
