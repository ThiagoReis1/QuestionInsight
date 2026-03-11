var=int(input("Digite o consumo de energia: "))

if (var <= 150):
	mensagem=0.60 * var + 5
	
else:
	mensagem= 0.75 * var + 16
	
print(round(mensagem, 2))