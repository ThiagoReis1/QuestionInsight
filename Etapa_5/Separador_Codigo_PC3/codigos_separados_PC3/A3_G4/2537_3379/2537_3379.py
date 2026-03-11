v = round(float(input("Insira o valor da herenca ")),2)
m = float(input("Insira o valor do saque mensal "))
j = float(input("Insira o valor da taxa de juros em porcentagem "))
if (v > 0 and m > 0 and j > 0):
	t = 1
	soma = 0
	while (v < (v + (v / 100)*20)):
		soma = round((v + (v/100)*j) - m,2)
		t = t + 1
		print(t)
else: print("Dados incorretos")
		
		 
		