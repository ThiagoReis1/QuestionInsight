P1 = float(input("Qual e a nota da P1? "))
P2 = float(input("Qual e a nota da P2? "))
P3 = float(input("Qual e a nota P3? "))
P4 = float(input("Qual e a nota P4? "))

m = (P1 + P2 + P3 + P4) / 4

if(m >= 7):
	print(round(m, 2))
	print("Aprovado")
else:
	print(round(m, 2))
	print("Reprovado")