from math import*
V = float(input("premio R$"))
M = float(input("Saque mensal: "))
j = float(input("Taxa de juros: "))

ps = V + V/100 * 10
t = 0
s = V

if(V > 0) and (M > 0) and (j > 0):
	while (s < ps):
		s = s + (s/100*10)
		s = round(s - M, 2)
		t = t + 1
	print(t)
else:
	mensagem = "Dados incorretos"
	print(mensagem)