pit = float(input("Digite a populacao inicial de tracajas:"))
taxa = float(input("Taxa anual de crescimento:"))
roubados = float(input("Numero de tracajas roubados anualmente:"))
n = 500
i = 1
soma = 0
while(pit > 0):
	cresc = pit * taxa
	pit = pit + cresc - roubados - n
	soma = soma + pit
	i = i + 1
print(i)