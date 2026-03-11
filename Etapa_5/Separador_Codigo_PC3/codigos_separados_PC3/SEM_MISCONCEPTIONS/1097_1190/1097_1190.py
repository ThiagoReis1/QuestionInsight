num = int(input("Digite um numero: "))
quoc = num // 1000
resto = num % 1000
teste = (quoc - resto) ** 2
if (teste == num):
	print(num, "atende a propriedade")
else:
	print(teste)