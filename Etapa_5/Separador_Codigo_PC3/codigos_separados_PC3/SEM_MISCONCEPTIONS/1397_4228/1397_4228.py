A = int(input("area a ser fertilizada(em Hectares): "))
E = ((A - 10000) * 4)

if (A <= 10000):
	mensagem = (A * 5)
else: 
	mensagem = ((10000 * 5) + E)

print(round(mensagem, 2))