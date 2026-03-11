# Ana Regina dos Santos da Silva - Mat. 21603561


Nota1 = float(input("Digite Nota1: "))
Nota2 = float(input("Digite Nota2: "))
Nota3 = float(input("Digite Nota3: "))
Nota4 = float(input("Digite Nota4: "))
Nota5 = float(input("Digite Nota5: "))

ma = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5) / 5

if (ma >= 6):
	print(round(ma,2))
	print("Aprovado")
	
else:
	if (ma < 6):
		print(round(ma,2))
		print("Reprovado")
	
