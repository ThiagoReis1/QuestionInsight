V = float(input("Valor da Heranca:"))
M = float(input("Saque Mensal fixo:"))
j = float(input("Taxa de Juros:"))

jpc = j / 100
sup = 1.2 * V
tempo = 0

if (V < 0 or M < 0 or j < 0):
	print("Dados incorretos")
else:
	while(V > sup):
		tH = (V - M) * jpc
		tH1 = round(tH,2)
		V = (V - M) + tH1
		tempo = tempo + 1
	print(tempo)	
		