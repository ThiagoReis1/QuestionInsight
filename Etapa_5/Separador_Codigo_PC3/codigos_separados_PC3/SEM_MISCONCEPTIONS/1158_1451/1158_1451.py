inicial = float(input("Digite a populaçao inicial: "))
taxa = float(input("Digite a taxa anual de crescimento: "))
roubados = float(input("Digite o numero de roubados: "))
q = inicial
n = 500
soma = 0
i = 1
while(q > 0):
	cresc = q * taxa
	q = q + cresc - roubados - n
	soma = soma + q
	i = i + 1 
print(i)