numero = float(input())
inteiro_k = int(input())

cont = 1
acum = 2
serie = numero

while(cont < inteiro_k):
	if (acum % 2 == 0):
		serie = serie - ((numero ** acum) / acum)
	else:
		serie = serie + ((numero ** acum) / acum)
	cont = cont + 1
	acum = acum + 1
print(round(serie, 10))
		
