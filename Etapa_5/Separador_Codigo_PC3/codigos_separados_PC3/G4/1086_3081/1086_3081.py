p1 = float(input("Digite a nota: "))
p2 = float(input("Digite a nota: "))
p3 = float(input("Digite a nota: "))
S = (p1 + p2 + p3)/3
if(S >= 7 ):
	print(round(S,1))
	print("Aprovado")
else:
	print(round(S,1))
	print("Reprovado")