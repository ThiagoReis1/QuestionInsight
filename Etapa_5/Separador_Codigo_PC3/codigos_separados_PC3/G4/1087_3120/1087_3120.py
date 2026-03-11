P1 = float(input("P1: "))
P2 = float(input("P2: "))
P3 = float(input("P3: "))
P4 = float(input("P4: "))

S = (P1 + P2 + P3 + P4) / 4

if (S >= 7.0):
	mensagem = "Aprovado"
else: 
	mensagem = "Reprovado"
	
print(round(S, 2))
print(mensagem)