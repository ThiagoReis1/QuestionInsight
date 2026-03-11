numero = int(input())

copia = numero

i = 1
parte_restante = ""
while i <= 3:
	parte_2 = numero % 10
	parte_restante =  str(parte_2) + parte_restante
	numero = numero // 10
	i = i + 1
print(copia)
if ((numero - int(parte_restante)) ** 4) == copia:
	print("atende")
else:
	print("nao atende")
