resposta = input("digite SIM ou NAO: ")
j = 0
i = 0
soma = 0
soma1 = 0

while(resposta.upper() != "S"):
	if (resposta.upper() == "SIM"):
		j = j + 1
		i = i + 1
		soma1 = soma1 + 1
		
	if (resposta.upper() == "NAO"):
		j = j + 1
		i = i + 1
		soma = soma + i
	resposta = input("digite SIM ou NAO: ")
a = (soma1/j)*100
print(i)
print(round(a, 2))
